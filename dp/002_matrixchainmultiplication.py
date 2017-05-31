#!/usr/bin/python
# -*- coding: utf-8 -*-


import random
import sys


def genMatrixDimension(a=2, b=20, length=5):
    madi = list()
    for i in range(length + 1):
        madi.append(random.randint(a, b))
    return madi


def genMatrix(madi):
    matrix = list()
    for i in range(len(madi) - 1):
        matrix.append((madi[i], madi[i + 1]))
    return matrix


# http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
def MatrixChain(p, n):
    m = [[0 for i in range(n)] for j in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L -1
            m[i][j] = sys.maxint
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i -1] * p[k] * p[j]
                if q<m[i][j]:
                    m[i][j] = q
    return m[1][n - 1]


if __name__ == "__main__":
    a = [4, 10, 3, 12, 20, 7]
    print(a)
    b = MatrixChain(a, len(a))
    print(b)
