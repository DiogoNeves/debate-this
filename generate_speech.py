import os
from dotenv import load_dotenv

from elevenlabs import play, save
from elevenlabs.client import ElevenLabs

# Load environment variables
load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=api_key)


text = '''"How dare you interrupt me while I'm working!" - he shouted angrily.
"This is absolutely ridiculous," -he growled in frustration.
"I can't believe I have to deal with this nonsense!" - he exclaimed.
"ENOUGH!" - he bellowed with rage.
"I've had it with these constant disruptions!"'''


def generate_speech():
    audio = client.generate(
        text=text,
        voice="Brian",
        model="eleven_multilingual_v2"
    )

    output_path = "output/speech.mp3"
    save(audio, output_path)
    print(f"Audio file generated successfully: {output_path}")


if __name__ == "__main__":
    generate_speech()
