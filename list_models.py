import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

# Load environment variables
load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=api_key)


def print_models() -> None:
    print("Requesting models")
    models = client.models.get_all()

    print("Available models:")
    for model in models:
        if not model.can_do_text_to_speech:
            continue
        print(f"- {model.name} (ID: {model.model_id})")
        print(f"  Description: {model.description}")
        print()


if __name__ == "__main__":
    print_models()
