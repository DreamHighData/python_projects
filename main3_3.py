from gtts import gTTS
from playsound import playsound
import os


file_path = 'my_text.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='en')
tts.save(r"voice/myText.mp3")
playsound(r"voice/myText.mp3")
