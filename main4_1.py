
# qrcode 다양한 코드를 확인 : https://pypi.org/project/qrcode/
import qrcode

qr_data = 'www.naver.com'

# qrcode.make로 이미지를 만들어 qr_img 변수에 바인딩합니다.
qr_img=qrcode.make(qr_data)
save_path =  "QR_code//" + qr_data + ".png"

qr_img.save(save_path)