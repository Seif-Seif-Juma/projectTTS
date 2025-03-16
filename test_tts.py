from TTS.api import TTS

def list_available_models():
    print("Available Models:")
    tts = TTS()
    models = tts.list_models()
    tts_models = models.list_tts_models()
    for i, model in enumerate(tts_models, 1):
        print(f"{i}. {model}")

def generate_speech(text, model_name="tts_models/en/ljspeech/vits", output_file="output.wav"):
    try:
        print(f"\nInitializing TTS with model: {model_name}")
        tts = TTS(model_name=model_name)
        
        print(f"\nGenerating speech for text:\n\"{text}\"\n")
        tts.tts_to_file(text=text, file_path=output_file)
        print(f"\nAudio generated successfully in: {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # List available models
    list_available_models()
    
    # Test speech generation with default model
    sample_text = "Hello! This is a test of the text to speech system."
    generate_speech(sample_text)
