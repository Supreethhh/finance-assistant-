import whisper
import pyttsx3
import tempfile

model = whisper.load_model("base")
engine = pyttsx3.init()


def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']


def speak_text(text):
    engine.say(text)
    engine.runAndWait()



