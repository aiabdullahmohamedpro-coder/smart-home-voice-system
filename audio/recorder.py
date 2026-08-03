from pathlib import Path

SAMPLE_RATE = 16000
DURATION = 3


def record_audio():
    """
    Record audio from microphone (Local only).
    """

    try:
        import sounddevice as sd
        from scipy.io.wavfile import write
    except Exception:
        raise RuntimeError(
            "Microphone recording is not available on this environment. "
            "Use Streamlit audio_input() when running on Streamlit Cloud."
        )

    output_folder = Path("temp")
    output_folder.mkdir(exist_ok=True)

    filename = output_folder / "input.wav"

    print("Recording...")

    recording = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
    )

    sd.wait()

    write(filename, SAMPLE_RATE, recording)

    print("Recording Finished.")

    return str(filename)