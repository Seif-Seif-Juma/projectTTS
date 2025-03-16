from TTS.api import TTS

# Initialize TTS with the simplest English model
tts = TTS(model_name="tts_models/en/ljspeech/fast_pitch")

# Simple test
text = "Hello! This is a test of the text to speech system."
print(f"Generating speech for: {text}")

# Generate the audio
tts.tts_to_file(text=text, file_path="test_output.wav")
print("Audio generated in test_output.wav")
