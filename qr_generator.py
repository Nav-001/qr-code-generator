import qrcode

def generate_qr():
    data = input("Enter text or URL: ").strip()

    if not data:
        print("Please enter some text or a URL.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=6,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(
        fill_color="black",
        back_color="grey"
    )

    filename = "QR_Code.png"
    qr_image.save(filename)

    print(f"QR code generated successfully: {filename}")

if __name__ == "__main__":
    generate_qr()
