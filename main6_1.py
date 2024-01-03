import itertools
import zipfile


def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len+1):
        to_attempt = itertools.product(passwd_string, repeat = len)

        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd = passwd.encode())
                print(f"Password is {passwd}")

                # 함수의 Return을 이용하여 함수 값을 넘기고 종료
                return 1
            except:
                pass


passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r"/Users/sunghwanki/Desktop/Project/python_projects/Password/password1234.zip")

min_len = 4
max_len = 5

unzip_result = un_zip(passwd_string, min_len, max_len, zFile)

if unzip_result == 1:
    print("Password is found successfully")
else:
    print("Failed")