# app.py

import streamlit as st
from clone import generate_voice
from pathlib import Path

st.set_page_config(page_title="AI Voice Cloner", layout="centered")
st.title("🎙️ AI Voice Cloner")
st.markdown("Upload a sample voice and enter text to clone the voice using AI (Coqui TTS).")

uploaded_file = st.file_uploader("Upload a voice sample (.wav)", type=["wav"])
text_input = st.text_area("Enter the text to speak")

if uploaded_file and text_input:
    speaker_path = "samples/input.wav"
    output_path = "outputs/cloned.wav"

    Path("samples").mkdir(exist_ok=True)
    Path("outputs").mkdir(exist_ok=True)

    with open(speaker_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ Generating voice... Please wait.")
    generate_voice(text_input, speaker_path, output_path)

    st.audio(output_path)
    with open(output_path, "rb") as f:
        st.download_button("⬇️ Download Cloned Voice", f, "cloned.wav")
