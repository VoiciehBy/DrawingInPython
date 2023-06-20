from numpy import array
from point import point
from color import color as Color
from color import blue, cyan, red
from utils import putColor, distanceOf
from math import fabs as math_fabs


def drawLineLow(image: array, start: point, end: point, color: Color):
    x: int = int(start.x)
    y: int = int(start.y)

    dX: int = int(end.x - start.x)
    dY: int = int(end.y - start.y)
    yI: int = 1

    dA: int = int(2 * dY)
    dB: int = int(2 * (dY - dX))

    if dY < 0:
        yI = -1
        dY = -dY

    d: int = int(dA - dX)
    while x < end.x:
        if d < 0:
            d += dA
        else:
            d += dB
            y += yI
        putColor(image, point(x, y), color)
        x += 1


def drawLineHigh(image: array, start: point, end: point, color: Color):
    x: int = int(start.x)
    y: int = int(start.y)

    dX: int = int(end.x - start.x)
    dY: int = int(end.y - start.y)
    xI: int = 1

    dA: int = int(2 * dX)
    dB: int = int(2 * (dX - dY))

    if dX < 0:
        xI = -1
        dX = -dX

    d: int = int(dA - dY)
    while y < end.y:
        if d < 0:
            d = d + dA
        else:
            d += dB
            x += xI
        putColor(image, point(x, y), color)
        y += 1


def drawLine(image: array, start: point, end: point, color: Color):
    x: int = int(start.x)
    y: int = int(start.y)
    putColor(image, point(x, y), color)

    if math_fabs(end.y - start.y) < math_fabs(end.x - start.x):
        if start.x > end.x:
            drawLineLow(image, end, start, color)
        else:
            drawLineLow(image, start, end, color)
    else:
        if start.y > end.y:
            drawLineHigh(image, end, start, color)
        else:
            drawLineHigh(image, start, end, color)


def drawTriangle(image: array, A: point, B: point, C: point):
    a = distanceOf(A, B)
    b = distanceOf(B, C)
    c = distanceOf(C, A)
    if(((a + b) > c) and ((b + c) > a) and ((a + c) > b)):
        drawLine(image, A, B, blue)
        drawLine(image, A, C, cyan)
        drawLine(image, B, C, red)


def drawsEightDrawPoints(image: array, a, o, color):
    putColor(image, point(o.x+a.x, o.y+a.y), color)
    putColor(image, point(o.x+a.y, o.y+a.x), color)
    putColor(image, point(o.x+a.y, o.y-a.x), color)
    putColor(image, point(o.x+a.x, o.y-a.y), color)
    putColor(image, point(o.x-a.x, o.y-a.y), color)
    putColor(image, point(o.x-a.y, o.y-a.x), color)
    putColor(image, point(o.x-a.y, o.y+a.x), color)
    putColor(image, point(o.x-a.x, o.y+a.y), color)


def drawCircle(image: array, o, radius, color: Color):
    x = 0
    y = radius
    d = 3 - 2*radius
    drawsEightDrawPoints(image, point(x, y), o, color)
    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x-y) + 10
        else:
            d = d + 4 * x + 6
        drawsEightDrawPoints(image, point(x, y), o, color)
