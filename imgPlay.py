import pipInstall
import utils
import color
import point
import draw
import cv2
import transforms

def installDependencies():
    pipInstall.pip_install("opencv-python")

def test():
    width = 800
    height = 600
    scale = 1
    image = utils.generateSolidImage(width, height, color.yellow)

    A = point.point(5*scale, 5*scale)
    B = point.point(120*scale, 80*scale)
    C = point.point(60*scale, 60*scale)

    draw.drawTriangle(image, A, B, C)
    draw.drawCircle(image, B, 25*scale, color.blue)
    cv2.imwrite("line.tiff", image)

def test1():
    A = point.point(1, 1)
    T = point.point(2,2)
    B = transforms.scale(A, T)
    C = transforms.translate(A,T)
    print(B.array)
    print(C.array)