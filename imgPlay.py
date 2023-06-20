from utils import generateSolidImage, showImage
from numpy import array
from color import yellow, blue
from point import point
from draw import drawTriangle, drawCircle
from cv2 import imwrite as cv2_imwrite

from transforms import scale as t_scale
from transforms import translate as t_translate


def test():
    width: int = 800
    height: int = 600
    scale: int = 1
    image: array = generateSolidImage(width, height, yellow)

    A: point = point(5*scale, 5*scale)
    B: point = point(120*scale, 80*scale)
    C: point = point(60*scale, 60*scale)

    drawTriangle(image, A, B, C)
    drawCircle(image, B, 25*scale, blue)
    cv2_imwrite("test.tiff", image)
    cv2_imwrite("test.png", image)
    showImage(image)


def test1():
    A: point = point(1, 1)
    T: point = point(2, 2)
    B: matrix = t_scale(A, T)
    C: matrix = t_translate(A, T)
    print(B.array)
    print(C.array)
