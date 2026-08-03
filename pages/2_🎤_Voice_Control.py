import os
import tempfile
import streamlit as st

from components.header import show_header
from utils.state import initialize_state
from services.voice_service import start_listening


st.set_page_config(
    page_title="Voice Control",
    page_icon="🎤",
    layout="wide"
)

initialize_state()

show_header()

st.title("🎤 Voice Assistant")

st.write("Control your smart home using your voice.")

st.divider()


IS_STREAMLIT_CLOUD = True


if IS_STREAMLIT_CLOUD:

    audio = st.audio_input("🎤 Record Command")

    if audio is not None:

        st.success("Audio received successfully.")

        # Save browser audio temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as temp_audio:

            temp_audio.write(audio.read())

            audio_path = temp_audio.name


        with st.spinner("Processing voice..."):

            result = start_listening(audio_path)


        st.success("Voice processed successfully!")


else:

    if st.button(
        "🎙 Start Listening",
        use_container_width=True
    ):

        with st.spinner("Listening..."):

            result = start_listening()

        st.success("Voice processed successfully!")


st.divider()


# =====================================
# Results
# =====================================

col1, col2 = st.columns(2)


with col1:

    st.metric(
        "👤 Speaker",
        st.session_state.last_user
    )

    st.metric(
        "🎯 Command",
        st.session_state.last_command
    )


with col2:

    st.metric(
        "📈 Confidence",
        f"{st.session_state.confidence:.2f}%"
    )

    st.metric(
        "🎤 Status",
        st.session_state.voice
    )


st.divider()

st.subheader("📝 Last Action")

st.info(
    f"Last command: {st.session_state.last_command}"
)