from TTS.api import TTS
import time

def list_available_models():
    print("Fetching available models...")
    tts = TTS()
    models = tts.list_models()
    
    # Get all TTS models
    tts_models = models.list_tts_models()
    
    print("\nAvailable TTS Models:")
    print("-" * 50)
    for idx, model in enumerate(tts_models, 1):
        lang = model.get('language', 'N/A')
        name = model.get('name', 'N/A')
        dataset = model.get('dataset', 'N/A')
        print(f"{idx}. Language: {lang}")
        print(f"   Name: {name}")
        print(f"   Dataset: {dataset}")
        print()

def test_xtts_adam():
    print("Initializing XTTS model (includes Adam voice)...")
    
    # Initialize XTTS model
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")
    
    text = "Hello! This is the Adam voice from XTTS model. It's one of the most popular male voices available."
    print(f"\nGenerating speech with Adam voice: \n\"{text}\"")
    
    # Generate speech using Adam voice
    tts.tts_to_file(
        text=text,
        file_path="adam_voice.wav",
        speaker_wav="adam", # This will use the built-in Adam reference
        language="en"
    )
    print("\nAdam voice sample saved as 'adam_voice.wav'")

def main():
    print("TTS Voice Testing Program")
    print("=" * 50)
    
    # List all available models
    list_available_models()
    
    # Test XTTS with Adam voice
    print("\nTesting XTTS model with Adam voice...")
    test_xtts_adam()
    
    print("\nNote: You can use the XTTS model with any reference voice by providing a WAV file!")

if __name__ == "__main__":
    main()
