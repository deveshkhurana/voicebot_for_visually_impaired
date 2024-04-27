#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:43:44 2024

@author: stlp
"""

from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def speech_to_text(audio_data):
    transcript = pipe(audio_data)['text']
    return transcript
