from ai.predict import verify_password


def authenticate(audio_path: str | None = None):

    # Cloud mode: audio already recorded from browser
    if audio_path is not None:
        return verify_password(audio_path)

    # Local mode: record from microphone
    from audio.recorder import record_audio

    path = record_audio()

    return verify_password(path)