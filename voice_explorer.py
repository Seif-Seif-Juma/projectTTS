from TTS.api import TTS
import argparse
import sys
import torch
from TTS.tts.configs.xtts_config import XttsConfig
import time
import os

# Add safe globals for PyTorch
torch.serialization.add_safe_globals([XttsConfig])

RECOMMENDED_VOICES = {
    "male_british": "tts_models/en/vctk/vits",
    "female_us": "tts_models/en/ljspeech/vits",
    "jenny": "tts_models/en/jenny/jenny",
    "fast": "tts_models/en/ljspeech/fast_pitch",
    "multi_speaker": "tts_models/multilingual/multi-dataset/your_tts",
    "high_quality": "tts_models/en/blizzard2013/capacitron-t2-c150_v2"
}

def generate_speech(text, model_name, output_file, speaker=None, language="en"):
    try:
        print(f"\nInitializing model: {model_name}")
        tts = TTS(model_name=model_name)
        
        kwargs = {
            "text": text,
            "file_path": output_file
        }
        
        if "multilingual" in model_name:
            kwargs["language"] = language
            if speaker:
                kwargs["speaker"] = speaker
        
        print(f"Generating speech for: \"{text}\"")
        start_time = time.time()
        tts.tts_to_file(**kwargs)
        duration = time.time() - start_time
        
        print(f"✓ Generated successfully in {duration:.2f} seconds")
        print(f"✓ Saved to: {output_file}")
        return True
    
    except Exception as e:
        print(f"Error with {model_name}: {str(e)}")
        return False

def demo_voices(text="This is a test of different voice models."):
    print("\nDemonstrating different voices...")
    
    test_cases = [
        ("British Voice", RECOMMENDED_VOICES["male_british"]),
        ("US Female Voice", RECOMMENDED_VOICES["female_us"]),
        ("Jenny Voice", RECOMMENDED_VOICES["jenny"]),
        ("Fast Voice", RECOMMENDED_VOICES["fast"]),
    ]
    
    results = []
    for voice_name, model in test_cases:
        print(f"\n=== Testing {voice_name} ===")
        output_file = f"demo_{voice_name.lower().replace(' ', '_')}.wav"
        success = generate_speech(text, model, output_file)
        if success:
            results.append(output_file)
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Voice Explorer - Test different TTS voices")
    parser.add_argument("--text", "-t", default="This is a test of the text to speech system.", 
                       help="Text to convert to speech")
    parser.add_argument("--demo", "-d", action="store_true", 
                       help="Run demo of different voices")
    parser.add_argument("--model", "-m", choices=RECOMMENDED_VOICES.keys(),
                       help="Choose a specific voice model")
    parser.add_argument("--output", "-o", default="output.wav",
                       help="Output file name")
    parser.add_argument("--speaker", "-s", 
                       help="Speaker name for multi-speaker models")
    
    args = parser.parse_args()
    
    if args.demo:
        generated_files = demo_voices(args.text)
        print("\nDemo files generated:")
        for file in generated_files:
            print(f"- {file}")
    
    elif args.model:
        model_name = RECOMMENDED_VOICES[args.model]
        generate_speech(args.text, model_name, args.output, args.speaker)
    
    else:
        print("\nAvailable voice types:")
        for key, model in RECOMMENDED_VOICES.items():
            print(f"- {key}: {model}")
        print("\nUse --demo to test different voices or --model to choose a specific voice.")

if __name__ == "__main__":
    main()
