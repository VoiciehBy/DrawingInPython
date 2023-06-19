from matrix import matrix
from point import point


def multiply(A, B) -> matrix:
    C: matrix = matrix(A.n, B.m)
    if(A.m == B.n):
        for i in range(0, A.n):
            for j in range(0, C.m):
                for k in range(0, B.m):
                    C.array[i][j] += A.array[i][k] * B.array[k][j]
    return C


def row_vector(a) -> matrix:
    A: matrix = matrix(2, 1)
    A.array[0][0] = a.x
    A.array[1][0] = a.y
    return A


def translate(a: point, t: point) -> matrix:
    return row_vector(point(a.x + t.x, a.y+t.y))


def scaling_ratio(sX: int, sY: int) -> matrix:
    S: matrix = matrix(2, 2)
    S.array[0][0] = sX
    S.array[1][1] = sY
    return S


def scale(a: point, t: point) -> matrix:
    S: matrix = scaling_ratio(t.x, t.y)
    A: matrix = row_vector(a)
    return multiply(A, S)
