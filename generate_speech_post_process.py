import requests
import os
import json
import base64
import ffmpeg
import tempfile
from dataclasses import dataclass
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

TEXT_TO_SPEECH_URL = "https://api.elevenlabs.io/v1/text-to-speech"


@dataclass
class Alignments:
    characters: list[str]
    character_start_times_seconds: list[float]
    character_end_times_seconds: list[float]


Range = tuple[int, int]


def _get_headers():
    api_key = os.getenv("ELEVENLABS_API_KEY")
    return {
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }


def _parse_response(response: requests.Response) -> tuple[bytes, Alignments]:
    json_string = response.content.decode("utf-8")
    response_dict = json.loads(json_string)

    audio_bytes = base64.b64decode(response_dict["audio_base64"])
    return audio_bytes, Alignments(**response_dict["alignment"])


def _get_ranges_to_keep(alignment: Alignments) -> list[tuple[int, int]]:
    """Create a list of start and end time ranges, in seconds, to keep in the
    audio.
    
    The text we want to keep is enclosed in double quotes.
    
    Example input:
    ```
    "This is the text we want to keep." - he said.
    "Another text." - she said.
    ```
    We want to keep:
    ```
    This is the text we want to keep.
    Another text.
    ```
    Excluding quotes.
    """
    ranges = []
    start = None

    for i, character in enumerate(alignment.characters):
        if character == '"':
            if start is None:
                start = alignment.character_end_times_seconds[i]
            else:
                ranges.append((start, alignment.character_start_times_seconds[i]))
                start = None

    return ranges


def _get_speech_from_audio(audio_bytes: bytes,
                           ranges_to_keep: list[Range]) -> bytes:
    """Extract the relevant speech from the audio bytes, using the provided
    time ranges.
    """
    # Create a simple temporary audio file. Simplifies the input to ffmpeg.
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_input:
        temp_input.write(audio_bytes)
        temp_input_path = temp_input.name

    inputs = [ffmpeg.input(temp_input_path, ss=start, to=end)
              for start, end in ranges_to_keep]
    output, _ = (
        ffmpeg
            .concat(*inputs, v=0, a=1)
            .output("pipe:", format="mp3")
            .run(capture_stdout=True, capture_stderr=True)
    )

    os.remove(temp_input_path)

    return output


def _save_audio(audio_bytes: bytes, file_name: str) -> None:
    output_path = f"output/{file_name}.mp3"
    with open(output_path, "wb") as f:
        f.write(audio_bytes)

    print(f"Audio file generated successfully: {output_path}")


def generate_speech():
    voice_id = "21m00Tcm4TlvDq8ikWAM"  # Rachel
    url = f"{TEXT_TO_SPEECH_URL}/{voice_id}/with-timestamps"

    text = '''The following should be played as two people argument at work.
Fast pace frustration and anger, high energy.
"How dare you interrupt me while I'm working!" - she shouted angrily.
"This is absolutely ridiculous," - she expressed in frustration.
"I can't believe I have to deal with this nonsense!" - she exclaimed.
"ENOUGH!" - she exclaimed with rage.
"I've had it with these constant disruptions!"'''

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(
        url,
        json=data,
        headers=_get_headers(),
    )
    response.raise_for_status()

    raw_audio_bytes, alignment = _parse_response(response)
    
    # We have to extract the relevant speech from the audio
    ranges_to_keep = _get_ranges_to_keep(alignment)
    real_speech_audio_bytes = _get_speech_from_audio(raw_audio_bytes,
                                                     ranges_to_keep)

    _save_audio(raw_audio_bytes, "raw")
    _save_audio(real_speech_audio_bytes, "post_process")

    print("Post-process completed successfully.")


if __name__ == "__main__":
    generate_speech()
