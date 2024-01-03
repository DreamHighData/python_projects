
# gtts 라이브러리로 부터 gTTS를 불러옵니다. 대문자에 유ㅠ의합니다.
from gtts import gTTS

text = "안녕하세요 파이썬 작품들입니다."
tts = gTTS(text=text, lang='ko')

# voice 폴더안에 mp3 파일 생성
# 문자열 앞에 r을 붙여주면 역슬레쉬를 그 의미대로 사용할 수 있음
# ../Python_Projects/voice 위치를 사용할 수 있음
tts.save(r"voice/hi.mp3")




