from TTS.api import TTS

def list_available_models():
    # Create TTS instance
    tts = TTS()
    
    # List available models
    print("Available Models:")
    models = tts.list_models()
    for i, model in enumerate(models):
        print(f"{i+1}. {model}")

if __name__ == "__main__":
    list_available_models()
