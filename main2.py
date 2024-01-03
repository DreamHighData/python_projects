import socket

# 내부 IP Address
# in_addr = socket.gethostbyname(socket.gethostname())

# socket으로 외부 사이트에 접속하고 접속된 내용을 바탕으로 내부 IP를 확인! 좀더 정확함
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))

print(in_addr.getsockname()[0])

