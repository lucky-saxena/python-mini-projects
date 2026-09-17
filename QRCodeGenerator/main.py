"""
Generates a QR code from a user-provided URL and saves it as a PNG file.
"""
import qrcode

url = input("Enter your url: ")
filename = input("Filename you want to save it as: ")
if not (filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)