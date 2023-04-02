import cv2
import numpy as np


def hiding(img_gray, Text):# text open in read mode (not binary)

    new_image = np.zeros(img_gray.shape, np.uint8)
    n,m = img_gray.shape

    # créer une copie de l'image original (on veut garder l'image originale )

    for i in range(n):
        for j in range(m):
            new_image[i][j] = image_gray[i][j]

    i,j = 0,0

    Text_content = Text + ((n*m)//8-len(Text)+1)*" " # pour que le reste de l'image n'affecte pas le contenue du texte

    for caracter in Text_content:
        Ascii = ord(caracter)
        binary = ("00000000"+bin(Ascii)[2:])[-8:]
        for b in binary:
            if i < n:
                if new_image[i][j]%2 != int(b):
                    if int(b) == 0:
                        new_image[i][j] = new_image[i][j]-1
                    else:
                        new_image[i][j] = new_image[i][j]+1
                j += 1
                if j == m:
                    j = 0
                    i += 1
    return new_image

def getting(image_hiding):
    Text = ""
    binary = ""
    n,m = image_hiding.shape
    for i in range(n):
        for j in range(m):
            binary += str(image_hiding[i][j]%2)
            if len(binary) == 8:
                Text += chr(int(binary,2))
                binary = ""
    return Text.rstrip()

# ------------------------------------------------------------------

Text = "RAMADAN KAREEM"

image = cv2.imread("Downloads/256niveaux.bmp")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_hiding = hiding(image_gray, Text)

Text2 = getting(image_hiding)

cv2.imshow("Originale", image_gray)
cv2.imshow("Hiding", image_hiding)
print("Hidden Text: ",Text2)
