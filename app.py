# app.py

import streamlit as st
from clone import generate_voice
from pathlib import Path

st.set_page_config(page_title="AI Voice Cloner", layout="centered")
st.title("🎙️ AI Voice Cloner")
st.markdown("Upload a sample voice and enter text to clone the voice using AI (Coqui TTS).")

uploaded_file = st.file_uploader("Upload a voice sample (.wav)", type=["wav"])
text_input = st.text_area("Enter the text to speak")
apply_button = st.button("🔊 Apply")

if apply_button:
    if not uploaded_file or not text_input:
        st.warning("⚠️ Please upload a voice sample and enter some text.")
    else:
        speaker_path = "samples/input.wav"
        output_path = "outputs/cloned.wav"

        Path("samples").mkdir(exist_ok=True)
        Path("outputs").mkdir(exist_ok=True)

        with open(speaker_path, "wb") as f:
            f.write(uploaded_file.read())

        st.info("🎤 Generating voice... Please wait.")
        generate_voice(text_input, speaker_path, output_path)

        st.success("✅ Cloning complete!")
        st.audio(output_path)

        with open(output_path, "rb") as f:
            st.download_button("⬇️ Download Cloned Voice", f, "cloned.wav")
