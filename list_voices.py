from TTS.api import TTS
import torch
from TTS.tts.configs.xtts_config import XttsConfig

def main():
    # Add XttsConfig to safe globals for PyTorch 2.6+
    torch.serialization.add_safe_globals([XttsConfig])
    
    print("Fetching available models...")
    tts = TTS()
    models = tts.list_models()
    
    print("\nAvailable TTS Models:")
    print("-" * 50)
    
    for idx, model in enumerate(models.list_tts_models(), 1):
        print(f"{idx}. {model}")
    
    print("\nRecommended models for different voices:")
    print("-" * 50)
    print("1. For multiple voices: tts_models/multilingual/multi-dataset/your_tts")
    print("2. For British accent: tts_models/en/vctk/vits")
    print("3. For US female voice: tts_models/en/ljspeech/tacotron2-DDC")
    print("4. For fast generation: tts_models/en/ljspeech/fast_pitch")

if __name__ == "__main__":
    main()
