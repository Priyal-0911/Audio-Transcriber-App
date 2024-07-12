import streamlit as st
import whisper
import torch
import io

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

st.title("Audio Transcription with Whisper")

# File uploader for audio file
audio_file = st.file_uploader("Upload an audio file", type=['mp3', 'wav'])

if audio_file is not None:
    # Read the audio file as bytes
    audio_bytes = audio_file.read()
    # Load Whisper model
    model = whisper.load_model('large').to(device)

    # Transcribe audio
    with open("/tmp/audio_tmp.mp3", "wb") as f:
        f.write(audio_bytes)

    audio = whisper.load_audio("/tmp/audio_tmp.mp3")
    text = whisper.transcribe(model=model, audio=audio)

    # Display transcription result
    st.subheader("Transcription Result:")
    st.write(text.get("text"))
