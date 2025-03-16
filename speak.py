
from TTS.api import TTS
import argparse
import sys

def generate_speech(text, output_file="output.wav", model_name="tts_models/en/ljspeech/vits"):
    try:
        print(f"\nInitializing TTS with model: {model_name}")
        tts = TTS(model_name=model_name)
        
        print(f"\nGenerating speech for text:\n\"{text}\"\n")
        tts.tts_to_file(text=text, file_path=output_file)
        print(f"\nAudio generated successfully in: {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate speech from text")
    parser.add_argument("text", help="The text to convert to speech")
    parser.add_argument("-o", "--output", default="output.wav", help="Output file name (default: output.wav)")
    parser.add_argument("-m", "--model", default="tts_models/en/ljspeech/vits", 
                       help="Model name (default: tts_models/en/ljspeech/vits)")
    
    args = parser.parse_args()
    generate_speech(args.text, args.output, args.model)
