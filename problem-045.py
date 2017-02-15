#!/usr/bin/python
# -*- coding: utf-8 -*-


from math import sqrt
from tools.runningTime import runTime


def generate_triangle(n=1, stop=None):
    if stop is None:
        stop = n+1
    while True:
        yield n*(n+1)/2
        n += 1
        if n == stop:
            break
    return

def generate_pentagonal(n=1, stop=None):
    if stop is None:
        stop = n+1
    while True:
        yield n*(3*n-1)/2
        n += 1
        if n == stop:
            break
    return

def generate_hexagonal(n=1, stop=None):
    if stop is None:
        stop = n+1
    while True:
        yield n*(2*n-1)
        n += 1
        if n == stop:
            break
    return

# very stupid method
@runTime
def bruteForce():
    # T285 = P165 = H143 = 40755
    n_tri = 286
    while True:
        x = generate_triangle(n_tri).next()
        y = generate_pentagonal(166, n_tri)
        while True:
            cachey = y.next()
            if cachey == x:
                z = generate_hexagonal(144, n_tri)
                while True:
                    cachez = z.next()
                    if cachez == x:
                        print "Result: {}".format(x)
                        return
                    elif cachez>x:
                        break
            elif cachey>x:
                break
        n_tri += 1
        if n_tri%100==0:
            print n_tri

# analysis problem first, please!
# hexagonal is a subset of triangle where n in triangle is replaced by 2*n-1.
@runTime
def newBruteForce():
    n = 144
    hexa = n*(2*n-1)
    while bool((sqrt(24*hexa+1)+1)/6%1):
        n += 1
        hexa = n*(2*n-1)
    print "Result: {}".format(hexa)

# Hexagonal Pentagonal Number
# http://mathworld.wolfram.com/HexagonalPentagonalNumber.html
# Diophantine equation
# https://en.wikipedia.org/wiki/Diophantine_equation
# Diophantine equation solver
# https://www.alpertron.com.ar/QUAD.HTM
@runTime
def byDiophantine():
    x, y = 165, 143
    P, Q, K = 97, 112, -44
    R, S, L = 84, 97, -38
    x, y = P*x+Q*y+K, R*x+S*y+L
    print "Result: {}".format(y*(2*y-1))


if __name__ == "__main__":
    # bruteForce()
    newBruteForce()
    byDiophantine()
