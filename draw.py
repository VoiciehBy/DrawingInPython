import point
import color
import utils
import math

def drawLineLow(image, start, end, color):
    x = start.x
    y = start.y

    dX = end.x - start.x
    dY = end.y - start.y
    yI = 1

    dA = 2 * dY
    dB = 2 * (dY - dX)
    if dY < 0:
        yI = -1
        dY = -dY

    d = dA - dX
    while x < end.x:
        if d < 0:
            d += dA
        else:
            d += dB
            y += yI
        utils.putColor(image, point.point(x, y), color)
        x += 1


def drawLineHigh(image, start, end, color):
    x = start.x
    y = start.y

    dX = end.x - start.x
    dY = end.y - start.y
    xI = 1

    dA = 2 * dX
    dB = 2 * (dX - dY)

    if dX < 0:
        xI = -1
        dX = -dX

    d = dA - dY
    while y < end.y:
        if d < 0:
            d = d + dA
        else:
            d += dB
            x += xI
        utils.putColor(image, point.point(x, y), color)
        y += 1


def drawLine(image, start, end, color):
    x = start.x
    y = start.y
    utils.putColor(image, point.point(x, y), color)

    if math.fabs(end.y - start.y) < math.fabs(end.x - start.x):
        if start.x > end.x:
            drawLineLow(image, end, start, color)
        else:
            drawLineLow(image, start, end, color)
    else:
        if start.y > end.y:
            drawLineHigh(image, end, start, color)
        else:
            drawLineHigh(image, start, end, color)


def drawTriangle(image, A, B, C):
    a = utils.distanceOf(A, B)
    b = utils.distanceOf(B, C)
    c = utils.distanceOf(C, A)
    if(((a + b) > c) and ((b + c) > a) and ((a + c) > b)):
        drawLine(image, A, B, color.blue)
        drawLine(image, A, C, color.cyan)
        drawLine(image, B, C, color.red)


def drawsEightDrawPoints(image, a, o, color):
    utils.putColor(image, point.point(o.x+a.x, o.y+a.y), color)
    utils.putColor(image, point.point(o.x+a.y, o.y+a.x), color)
    utils.putColor(image, point.point(o.x+a.y, o.y-a.x), color)
    utils.putColor(image, point.point(o.x+a.x, o.y-a.y), color)
    utils.putColor(image, point.point(o.x-a.x, o.y-a.y), color)
    utils.putColor(image, point.point(o.x-a.y, o.y-a.x), color)
    utils.putColor(image, point.point(o.x-a.y, o.y+a.x), color)
    utils.putColor(image, point.point(o.x-a.x, o.y+a.y), color)


def drawCircle(image, o, r, color):
    x = 0
    y = r
    d = 3 - 2*r
    drawsEightDrawPoints(image, point.point(x, y), o, color)
    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x-y) + 10
        else:
            d = d + 4 * x + 6
        drawsEightDrawPoints(image, point.point(x, y), o, color)