# clone.py

from TTS.api import TTS
from pathlib import Path

# Load model once (heavy)
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False)

def generate_voice(text, speaker_path, output_path):
    Path("outputs").mkdir(exist_ok=True)
    tts.tts_to_file(
        text=text,
        speaker_wav=speaker_path,
        language="en",
        file_path=output_path
    )
    return output_path
