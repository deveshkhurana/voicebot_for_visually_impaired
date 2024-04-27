#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:19:55 2024

@author: stlp
"""

import streamlit as st
import os
from stt import speech_to_text
from text_gen import get_answer
from tts import generate_speech
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *
from gtts import gTTS
import time
import tempfile


float_init()

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I am EyeNav, your personal Navigation assistant. How can I help you today?"}
        ]
        print("initialize_session_state called. Messages exist:", "messages" in st.session_state)
initialize_session_state()

st.title("Iris")

footer_container = st.container()
with footer_container:
    audio_bytes = audio_recorder()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if audio_bytes:
    with st.spinner("Transcribing..."):
        transcript = speech_to_text(audio_bytes)
        st.session_state.messages.append({"role": "user", "content": transcript})
        final_response = get_answer(st.session_state.messages)
        with st.chat_message("user"):
            st.write(transcript)
    
    with st.chat_message("assistant"):
        generate_speech(final_response)
        st.write(final_response)
        st.session_state.messages.append({"role": "assistant", "content": final_response})
        
    os.remove("tmp.mp3")
footer_container.float("bottom: 0rem;")
