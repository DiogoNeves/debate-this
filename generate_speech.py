import os
from dotenv import load_dotenv

from elevenlabs import play, save
from elevenlabs.client import ElevenLabs

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=api_key)


text = '''"How dare you interrupt me while I'm working!" he shouted angrily.
"This is absolutely ridiculous," he growled in frustration.
"I can't believe I have to deal with this nonsense!"
"ENOUGH!" he bellowed with rage.
"I've had it with these constant disruptions!"'''

audio = client.generate(
  text=text,
  voice="Brian",
  model="eleven_multilingual_v2"
)

play(audio)
save(audio, "output/speech.mp3")

print("Audio file generated successfully: output/speech.mp3")
