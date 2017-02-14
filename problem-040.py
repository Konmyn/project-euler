#!/usr/bin/python
# -*- coding: utf-8 -*-


from operator import mul
from tools.runningTime import runTime


@runTime
def bruteForce(L=7):
    natural, product, length = 1, 1, 0
    for i in range(L):
        while True:
            length += len(str(natural))
            if length >= 10**i:
                product *= int(str(natural)[((len(str(natural))-(length-10**i))-1)])
                natural += 1
                break
            natural += 1
    print "Result: {}".format(product)

def findigits(d):
    if d == 0 or d == 1:
        return 1
    # step is the digits of number and max_len is the total length
    # to the end of same digits ofthe number.
    step, max_len = 0, 0
    while max_len<10**d:
        step += 1
        max_len += (10**step-10**(step-1))*step
    max_len -= (10**step-10**(step-1))*step
    i, j = divmod(10**d-max_len, step)
    start = 10**(d-1)-1+i
    return int(str(start)[j-1])

# Champernowne constant
# https://en.wikipedia.org/wiki/Champernowne_constant
@runTime
def byFormula(L=7):
    digits = [0]*L
    for i, d in enumerate(digits):
        digits[i] = findigits(i)
    print "Result: {}".format(reduce(mul, digits, 1))


if __name__ == "__main__":
    bruteForce()
    byFormula()
