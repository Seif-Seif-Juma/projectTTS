from TTS.api import TTS
import argparse
import sys
import torch
from TTS.tts.configs.xtts_config import XttsConfig
import warnings
warnings.filterwarnings("ignore")

def generate_speech(text, output_file="output.wav", model_name=None, speaker_wav=None, language="en"):
    try:
        # Add XttsConfig to safe globals for PyTorch 2.6+
        torch.serialization.add_safe_globals([XttsConfig])
        
        # Use YourTTS model instead of XTTS v2 for better compatibility
        if model_name is None:
            model_name = "tts_models/multilingual/multi-dataset/your_tts"
        
        print(f"Initializing TTS with model: {model_name}")
        tts = TTS(model_name=model_name)
        
        print(f"\nGenerating speech for text:\n\"{text}\"\n")
        
        # Generate speech
        if speaker_wav == "adam":
            # For YourTTS, we can use speaker embeddings
            tts.tts_to_file(
                text=text,
                file_path=output_file,
                speaker="adam",  # Using predefined speaker
                language=language
            )
        else:
            tts.tts_to_file(
                text=text,
                file_path=output_file,
                language=language
            )
            
        print(f"\nAudio generated successfully in: {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("\nTrying alternative model...")
        try:
            # Fallback to a simpler model
            fallback_model = "tts_models/en/vctk/vits"
            print(f"Using fallback model: {fallback_model}")
            tts = TTS(fallback_model)
            tts.tts_to_file(text=text, file_path=output_file)
            print(f"\nAudio generated successfully with fallback model in: {output_file}")
        except Exception as e2:
            print(f"Fallback also failed: {str(e2)}")
            sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate speech from text with various voices")
    parser.add_argument("text", help="The text to convert to speech")
    parser.add_argument("-o", "--output", default="output.wav", help="Output file name (default: output.wav)")
    parser.add_argument("-s", "--speaker", help="Speaker (use 'adam' for Adam voice)")
    parser.add_argument("-l", "--language", default="en", help="Language code (default: en)")
    args = parser.parse_args()
    
    generate_speech(
        text=args.text,
        output_file=args.output,
        speaker_wav=args.speaker,
        language=args.language
    )
