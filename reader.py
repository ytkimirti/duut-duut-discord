from PIL import Image
from typing import List

def read(path="./test.png") -> List[str]:
    img = Image.open(path).convert("RGB")

    pixels = img.load()

    xlen, ylen = img.size

    arr = []
    for y in range(ylen):
        str = ""
        for x in range(xlen):
            char = " "
            c = pixels[x, y]
            r, g, b = c
            if r > 0 and g < 100 and b < 100:
                char = ":flag_no:"
            else:
                char = ":wheelchair:"
            str += char
        arr.append(str)
    return arr

if __name__ == "__main__":
    print(read())
