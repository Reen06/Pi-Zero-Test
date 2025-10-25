import qrcode

text = input("Enter text or URL to convert into a QR code:\n> ")

img = qrcode.make(text)
img.save("qr_code.png")

print("\n✅ QR code saved as qr_code.png")
