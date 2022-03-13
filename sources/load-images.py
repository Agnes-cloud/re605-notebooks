import cv2 as cv
import numpy as np
import random

# Lengkapi fungsi berikut ini agar dapat mengembalikan nilai intensitas warna merah
# dari gambar `img` pada koordinat pixel x, y
# gambar `img` merupakan sebuah sebuah gambar berwarna dengan color space BGR
def red_at_pixel(img, x, y):
    red = 0
    # tuliskan script anda disini
    red = img[y,x,2]
    # akhir script
    return red

# Lengkapi fungsi berikut ini agar dapat mengembalikan nilai intensitas warna hijau
# dari gambar `img` pada koordinat pixel x, y
# gambar `img` merupakan sebuah sebuah gambar berwarna dengan color space BGR
def green_at_pixel(img, x, y):
    green = 0
    # tuliskan script anda disini
    green = img[y,x,1]
    # akhir script
    return green

# Lengkapi fungsi berikut ini agar dapat mengembalikan nilai intensitas warna biru
# dari gambar `img` pada koordinat pixel x, y
# gambar `img` merupakan sebuah sebuah gambar berwarna dengan color space BGR
def blue_at_pixel(img, x, y):
    blue = 0
    # tuliskan script anda disini
    blue = img[y,x,0]

    # akhir script
    return blue

# Gunakan fungsi `main` untuk menguji-coba fungsi diatas
def main():
    print("=======================================")
    print("Exercise 1 - Reading Color Images")
    print("=======================================")
    
    bgr_img = cv.imread("./images/cat-image.jpg")
    x = random.randint(0, bgr_img.shape[1])
    y = random.randint(0, bgr_img.shape[0])
    red = red_at_pixel(bgr_img, x, y)
    green = green_at_pixel(bgr_img, x, y)
    blue = blue_at_pixel(bgr_img, x, y)

    print("Red value at {", x, y, "} = ", red)
    print("Green value at {", x, y, "} = ", green)
    print("Blue value at {", x, y, "} = ", blue)

if _name_ == "_main_":
    main()
