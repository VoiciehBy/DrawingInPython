import subprocess
import numpy
import cv2


def pip_install(packageName):
    subprocess.call(["pip", "install", packageName])


def installDependencies():
    pip_install("numpy")

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = numpy.zeros((n, m))


def multiply(A, B):
    C = matrix(A.n, B.m)
    if(A.m == B.n):
        for i in range(0,A.n):
            for j in range(0,C.m):
                for k in range(0,B.m):
                    C.matrix[i][j] += A.matrix[i][k] * B.matrix[k][j]
    return C


def translate(a, t):
    translated = point(a.x + t.x, a.y+t.y)
    return translated

def scaling_ratio(sX,sY):
    S = matrix(2,2)
    S.matrix[0][0] = sX
    S.matrix[1][1] = sY
    return S
    
def row_vector(a):
    A = matrix(2,1)
    A.matrix[0][0] = a.x
    A.matrix[1][0] = a.y
    return A

def scale(a,t):
    S = scaling_ratio(t.x,t.y)
    A = row_vector(a)
    return multiply(A, S)

def main():
    installDependencies()
    A = point(1, 1)
    T = point(2,2)
    B = scale(A, T)
    print(B.matrix)
main()
