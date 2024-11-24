import os
from dotenv import load_dotenv

from elevenlabs import play, save
from elevenlabs.client import ElevenLabs

# Load environment variables
load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=api_key)


text = '''Thank you for calling tech support, how may I assist you today?
Have you tried turning it off and on again?
Sir, please... just try turning it off and on!
JUST RESTART THE COMPUTER!'''


def generate_speech():
    audio = client.generate(
        text=text,
        voice="Rachel",
        model="eleven_multilingual_v2"
    )

    output_path = "output/speech.mp3"
    save(audio, output_path)
    print(f"Audio file generated successfully: {output_path}")


if __name__ == "__main__":
    generate_speech()
