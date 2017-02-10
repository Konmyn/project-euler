#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import factorial


# 0! is one!!!!!
FACTORIAL_DICT = {0: 1,}

def generate_factorial_dict():
    for i in range(1, 10):
        FACTORIAL_DICT[i] = factorial(i)

def digits_fac_sum(natural):
    the_sum = 0
    while natural:
        the_sum, natural = the_sum+FACTORIAL_DICT[natural%10], natural/10
    return the_sum

@runTime
def bruteForce():
    generate_factorial_dict()
    # 9!*7 = 2540160
    datas = []
    start, stop = 11, 2540160
    for natural in xrange(start, stop):
        if natural == digits_fac_sum(natural):
            datas.append(natural)
    print "Result: {}".format(sum(datas))

# These type of numbers are referred to as factorions
# and it’s easy to learn that only 4 exist: 1, 2, 145 & 40585.
# factorions = [1, 2, 145, 40585]
# Factorions: equal to the sum of the factorials of their digits in base 10.
# https://oeis.org/A014080
# https://en.wikipedia.org/wiki/Factorion

if __name__ == "__main__":
    bruteForce()
