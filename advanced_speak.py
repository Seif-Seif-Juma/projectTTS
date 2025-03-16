from TTS.api import TTS
import argparse
import sys

def generate_speech(text, output_file="output.wav", model_name=None, speaker_wav=None, language="en"):
    try:
        # Use XTTS by default if no model specified
        if model_name is None:
            model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
        
        print(f"Initializing TTS with model: {model_name}")
        tts = TTS(model_name=model_name)
        
        print(f"\nGenerating speech for text:\n\"{text}\"\n")
        
        # Generate speech with additional parameters if provided
        kwargs = {
            "text": text,
            "file_path": output_file,
        }
        
        # Add speaker_wav if provided
        if speaker_wav:
            kwargs["speaker_wav"] = speaker_wav
        
        # Add language if it's a multilingual model
        if "multilingual" in model_name:
            kwargs["language"] = language
        
        tts.tts_to_file(**kwargs)
        print(f"\nAudio generated successfully in: {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate speech from text with various voices")
    parser.add_argument("text", help="The text to convert to speech")
    parser.add_argument("-o", "--output", default="output.wav", help="Output file name (default: output.wav)")
    parser.add_argument("-m", "--model", help="Model name (default: XTTS v2)")
    parser.add_argument("-s", "--speaker", help="Speaker reference WAV file or 'adam' for Adam voice")
    parser.add_argument("-l", "--language", default="en", help="Language code (default: en)")
    args = parser.parse_args()
    
    generate_speech(
        text=args.text,
        output_file=args.output,
        model_name=args.model,
        speaker_wav=args.speaker,
        language=args.language
    )
