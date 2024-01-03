import qrcode

file_path = "QR_code/qr_code.txt"

with open(file_path, 'r', encoding='UTF8') as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = "QR_code//" + qr_data + ".png"
        qr_img.save(save_path)
        
        
        
        
        