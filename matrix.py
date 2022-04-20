import numpy


class matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.array = numpy.zeros((n, m))
