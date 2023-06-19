from cv2 import imshow, waitKey, destroyAllWindows, imwrite
from numpy import array, zeros, uint8
from point import point
from math import sqrt


def showImage(image: array):
    imshow("Image", image)
    waitKey(0)
    destroyAllWindows()


def putColor(image: array, a, color):
    bgr = color.to_bgr()
    image[a.y][a.x] = array(bgr)


def generateSolidImage(width: int, height: int, color) -> array:
    image: array = zeros((height, width, 3), uint8)
    for i in range(width):
        for j in range(height):
            putColor(image, point(i, j), color)
    imwrite("test.tiff", image)
    return image


def distanceOf(A: point, B: point):
    return sqrt((B.x-A.x)**2 + (B.y-A.y)**2 + (B.z-A.z)**2)


def length(A: point):
    return distanceOf(A, A)
