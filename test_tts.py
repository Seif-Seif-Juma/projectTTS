from TTS.api import TTS
from typing import List, Dict

def print_model_list(models: List[Dict], category: str):
    print(f"\n{category} Models:")
    print("-" * (len(category) + 8))
    for idx, model in enumerate(models, 1):
        print(f"{idx}. Language: {model.get('language', 'N/A')}")
        print(f"   Name: {model.get('name', 'N/A')}")
        print(f"   Dataset: {model.get('dataset', 'N/A')}")
        print()

def list_available_models():
    try:
        # Initialize TTS
        print("Initializing TTS...")
        tts = TTS()
        
        # Get available models using list_models()
        print("Fetching available models...")
        model_manager = tts.list_models()
        
        # Get specific model lists
        tts_models = model_manager.list_tts_models()
        vocoder_models = model_manager.list_vocoder_models()
        
        # Print TTS models
        print_model_list(tts_models, "Text-to-Speech")
        
        # Print Vocoder models
        print_model_list(vocoder_models, "Vocoder")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        import traceback
        print(traceback.format_exc())

if __name__ == "__main__":
    list_available_models()
