import sys
import string
from PIL import Image

def decode(img, key):
    image = Image.open(img, 'r')
    data = ''
    imgdata = iter(image.getdata())
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]]
        binstr = ''
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return cipher(data, key)


def cipher(text, shift):
    shift %= 67544
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

def main():
    # image name
    img = sys.argv[1]

    # decryption key
    key = int(sys.argv[2])

    text = decode(img, key)
    print("[+] Decoded:", text)

if __name__ == '__main__':
    main()
