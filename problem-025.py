#!/usr/bin/python
# -*- coding: utf-8 -*-


from math import log10, ceil, sqrt
from tools.runningTime import runTime


@runTime
def brute_force_method(digits=1000):
    i, j, n = 1, 1, 1
    while i < 10**(digits-1):
        i, j, n = j, i+j, n+1
    print "Result: {}".format(n)

# Binet's Fibonacci Number Formula
# http://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
@runTime
def from_binet(digits=1000):
    phi = (1+sqrt(5))/2
    index = int(ceil((digits-1+log10(5)/2)/log10(phi)))
    print "Result: {}".format(index)

if __name__ == "__main__":
    brute_force_method()
    from_binet()
