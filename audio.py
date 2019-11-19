"""
Created on 16 de mar de 2016

@author: fvj
"""
import math

import pyaudio


# 261.63=C4-note
def sine_tone(freq=440, length=1, bitrate=16000):
    if freq > bitrate:
        bitrate = freq + 100

    NUMBEROFFRAMES = int(bitrate * length)
    RESTFRAMES = NUMBEROFFRAMES % bitrate
    WAVEDATA = ""

    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA + chr(
            int(math.sin(x / ((bitrate / freq) / math.pi)) * 127 + 128)
        )

    for x in range(RESTFRAMES):
        WAVEDATA = WAVEDATA + chr(128)

    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(1), channels=1, rate=bitrate, output=True
    )

    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()
