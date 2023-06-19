from numpy import zeros


class matrix:
    def __init__(self, n: int, m: int):
        self.n = int(n)
        self.m = int(m)
        self.array = zeros((n, m))
