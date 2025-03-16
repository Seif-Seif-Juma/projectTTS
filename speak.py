from TTS.api import TTS
import sys
import argparse

def generate_speech(text, output_file="output.wav", model="tts_models/en/ljspeech/fast_pitch"):
    try:
        # Initialize TTS with the model
        print(f"Initializing TTS with model: {model}")
        tts = TTS(model_name=model)
        
        # Generate the audio
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
    args = parser.parse_args()
    
    generate_speech(args.text, args.output)
