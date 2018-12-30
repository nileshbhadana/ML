import speech_recognition as sr
import os
import socket 

mic=sr.Microphone()
r=sr.Recognizer()
with mic as source:
    r.adjust_for_ambient_noise(source)
    print('say')
    audio=r.listen(source)
audio_input=r.recognize_google(audio)
print(audio_input)
if 'open chrome' in audio_input.lower():
    os.system("chromium-browser")
elif 'make directory' in audio_input.lower():
    os.mkdir(audio_input.split()[2])
