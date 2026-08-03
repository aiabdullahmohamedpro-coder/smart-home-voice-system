import os
import tempfile
import streamlit as st

from components.header import show_header
from utils.state import initialize_state
from services.password_service import authenticate


st.set_page_config(
    page_title="Password",
    page_icon="🔐",
    layout="wide"
)

initialize_state()

show_header()

st.title("🔐 Smart Home Authentication")

st.write("Please say the password to unlock the Smart Home.")

st.divider()


IS_STREAMLIT_CLOUD = True


if IS_STREAMLIT_CLOUD:

    audio = st.audio_input("🎤 Record Password")

    if audio is not None:

        st.success("Audio received successfully.")

        # Save browser audio temporarily as wav
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as temp_audio:

            temp_audio.write(audio.read())

            audio_path = temp_audio.name


        with st.spinner("Checking password..."):

            result = authenticate(audio_path)


        if result.password_ok:

            st.success(result.message)
            st.session_state.authenticated = True

        else:

            st.error(result.message)
            st.session_state.authenticated = False


        st.write("**Transcript:**", result.transcript)


else:

    if st.button(
        "🎙 Record Password",
        use_container_width=True
    ):

        with st.spinner("Listening..."):

            result = authenticate()


        if result.password_ok:

            st.success(result.message)
            st.session_state.authenticated = True

        else:

            st.error(result.message)
            st.session_state.authenticated = False


        st.write("**Transcript:**", result.transcript)