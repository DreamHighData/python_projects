from gtts import gTTS
from playsound import playsound
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
# playsound에서 한글을 인식하지 못하여 경로를 이동
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
text = "안녕하세요 이것은 파이썬 프로젝트입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"voice/new_hi.mp3")

# 만약 playsound 가 작동하지 않는다면 pip install PyObjC 실행해줌
playsound(r"voice/new_hi.mp3")