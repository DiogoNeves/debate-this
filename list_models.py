import asyncio
import os
from dotenv import load_dotenv
from elevenlabs.client import AsyncElevenLabs

# Load environment variables
load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
eleven = AsyncElevenLabs(api_key=api_key)

async def print_models() -> None:
    print("Requesting models")
    models = await eleven.models.get_all()
    
    print("Available models:")
    for model in models:
        if not model.can_do_text_to_speech:
            continue
        print(f"- {model.name} (ID: {model.model_id})")
        print(f"  Description: {model.description}")
        print()

asyncio.run(print_models())
