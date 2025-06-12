import streamlit as st
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from processing.transcribe_audio import transcribe_audio
from processing.extract_fields import extract_crm_fields

# Create folders if not exist
os.makedirs("input", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

st.title("📥 CRMExtractorAI – Smart CRM Auto-Filler 🤖")

uploaded_file = st.file_uploader("Upload a .txt or .wav/.mp3 file", type=["txt", "wav", "mp3"])

if uploaded_file:
    file_path = os.path.join("input", uploaded_file.name)
    
    # Save file to disk
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Process file based on type
    if uploaded_file.name.endswith(".txt"):
        # Reopen from disk to ensure decoding works consistently
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        # Use audio transcription
        text = transcribe_audio(file_path)

    st.subheader("📝 Extracted Text")
    st.write(text)

    # Button to extract CRM fields
    if st.button("🚀 Extract CRM Fields"):
        extracted = extract_crm_fields(text)

        st.subheader("📊 Structured Output")
        st.json(extracted)

        # Save to output folder
        with open("outputs/structured_output.json", "w", encoding="utf-8") as out:
            json.dump(extracted, out, indent=4, ensure_ascii=False)

        st.success("✅ Extraction completed and saved to outputs/structured_output.json")
