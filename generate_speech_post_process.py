import requests
import os
import json
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TEXT_TO_SPEECH_URL = "https://api.elevenlabs.io/v1/text-to-speech"


def _get_headers():
    api_key = os.getenv("ELEVENLABS_API_KEY")
    return {
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }


def _parse_response(response: requests.Response) -> tuple[bytes, dict]:
    json_string = response.content.decode("utf-8")
    response_dict = json.loads(json_string)

    audio_bytes = base64.b64decode(response_dict["audio_base64"])
    return audio_bytes, response_dict["alignment"]


def _save_audio(audio_bytes: bytes) -> None:
    output_path = "output/post_process.mp3"
    with open(output_path, "wb") as f:
        f.write(audio_bytes)

    print(f"Audio file generated successfully: {output_path}")


def generate_speech():
    voice_id = "21m00Tcm4TlvDq8ikWAM"  # Rachel
    url = f"{TEXT_TO_SPEECH_URL}/{voice_id}/with-timestamps"

    text = '''"How dare you interrupt me while I'm working!" - he shouted angrily.
"This is absolutely ridiculous," -he growled in frustration.
"I can't believe I have to deal with this nonsense!" - he exclaimed.
"ENOUGH!" - he bellowed with rage.
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

    audio_bytes, alignment = _parse_response(response)
    _save_audio(audio_bytes)
    print(alignment)


if __name__ == "__main__":
    generate_speech()