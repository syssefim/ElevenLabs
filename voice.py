from elevenlabs import ElevenLabs
from elevenlabs.play import play
from dotenv import load_dotenv
import os

load_dotenv()
eleven_labs_api = os.getenv("ELEVEN_LABS_API_KEY")

def speak(script):
    client = ElevenLabs(api_key=eleven_labs_api)
    
    audio = client.text_to_speech.convert(
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        text=script,
        model_id="eleven_multilingual_v2",
    )

    play(audio)

