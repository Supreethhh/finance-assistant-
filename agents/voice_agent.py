from gtts import gTTS
import os

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    audio_file = "output.mp3"
    tts.save(audio_file)
    os.system("mpg123 output.mp3")  # Requires mpg123
