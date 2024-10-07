from PIL import Image
from pyzbar.pyzbar import decode

with Image.open("./frame003699.png") as img:
    results = decode(img)
    print(results)
