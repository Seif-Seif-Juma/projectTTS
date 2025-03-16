from TTS.api import TTS

def list_available_models():
    # List available models and choose the first English one
    print("Available Models:")
    models = TTS.list_models()
    for i, model in enumerate(models):
        print(f"{i+1}. {model}")

if __name__ == "__main__":
    list_available_models()
