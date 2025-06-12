from faster_whisper import WhisperModel

def transcribe_audio(audio_path):
    try:
        # Load the model (You can cache it globally if calling this multiple times)
        model = WhisperModel("base", compute_type="auto")  # 'auto' chooses best available device (GPU/CPU)

        # Transcribe the audio file
        segments, _ = model.transcribe(audio_path, beam_size=5)  # beam_size improves quality slightly

        # Combine all transcribed segments
        transcription = " ".join([segment.text.strip() for segment in segments])

        return transcription or "⚠️ Transcription returned empty."
    except Exception as e:
        return f"❌ Transcription error: {str(e)}"
