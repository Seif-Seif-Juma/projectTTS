from TTS.api import TTS
import argparse
import sys

def generate_speech(text, output_file="output.wav", speed=1.0):
    try:
        # Use the reliable LJSpeech VITS model
        model_name = "tts_models/en/ljspeech/vits"
        print(f"\nInitializing TTS with model: {model_name}")
        
        # Initialize TTS
        tts = TTS(model_name=model_name)
        
        print(f"\nGenerating speech for text:\n\"{text}\"\n")
        
        # Generate speech with speed adjustment
        tts.tts_to_file(
            text=text, 
            file_path=output_file,
            speed=speed  # Adjust speech rate (0.5 = slower, 1.5 = faster)
        )
        
        print(f"\n✓ Audio generated successfully!")
        print(f"✓ Saved to: {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate speech from text using LJSpeech VITS model")
    parser.add_argument("text", help="The text to convert to speech")
    parser.add_argument("-o", "--output", default="output.wav", help="Output file name (default: output.wav)")
    parser.add_argument("-s", "--speed", type=float, default=1.0, 
                       help="Speech speed (0.5 = slower, 1.0 = normal, 1.5 = faster)")
    
    args = parser.parse_args()
    
    # Validate speed parameter
    if args.speed < 0.5 or args.speed > 2.0:
        print("Speed must be between 0.5 and 2.0")
        sys.exit(1)
    
    generate_speech(args.text, args.output, args.speed)
