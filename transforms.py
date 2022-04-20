import numpy
import matrix
import point

def multiply(A, B):
    C = matrix.matrix(A.n, B.m)
    if(A.m == B.n):
        for i in range(0,A.n):
            for j in range(0,C.m):
                for k in range(0,B.m):
                    C.array[i][j] += A.array[i][k] * B.array[k][j]
    return C

def row_vector(a):
    A = matrix.matrix(2,1)
    A.array[0][0] = a.x
    A.array[1][0] = a.y
    return A

def translate(a, t):
    return row_vector(point.point(a.x + t.x, a.y+t.y))

def scaling_ratio(sX,sY):
    S = matrix.matrix(2,2)
    S.array[0][0] = sX
    S.array[1][1] = sY
    return S
    
def scale(a,t):
    S = scaling_ratio(t.x,t.y)
    A = row_vector(a)
    return multiply(A, S)
