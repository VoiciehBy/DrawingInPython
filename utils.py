import cv2
import color
import numpy
import point
import math

def showImage(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def putColor(image, a, color):
    image[a.y][a.x] = numpy.array(color.rgb)


def generateSolidImage(width, height, color):
    image = numpy.zeros((height, width, 3), numpy.uint8)
    for i in range(width):
        for j in range(height):
            putColor(image, point.point(i, j), color)
    cv2.imwrite("test.tiff", image)
    return image


def distanceOf(A, B):
    return math.sqrt((B.x-A.x)**2 + (B.y-A.y)**2 + (B.z-A.z)**2)

def length(A):
    return distanceOf(A, A)