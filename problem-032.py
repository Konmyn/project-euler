#!/usr/bin/python
# -*- coding: utf-8 -*-


import operator as op
from itertools import permutations
from tools.runningTime import runTime
from tools.common import is_pandigital as IP


@runTime
def bruteForce():
    products = set()
    for i in permutations(range(1,10)):
        if (i[0]*10+i[1])*(i[2]*100+i[3]*10+i[4]) == i[5]*1000+i[6]*100+i[7]*10+i[8]:
            products.add(i[5]*1000+i[6]*100+i[7]*10+i[8])
        if i[0]*(i[1]*1000+i[2]*100+i[3]*10+i[4]) == i[5]*1000+i[6]*100+i[7]*10+i[8]:
            products.add(i[5]*1000+i[6]*100+i[7]*10+i[8])
    print "Result: {}".format(sum(products))

@runTime
def newBruteForce():
    p = set()
    for i in range(2, 60):
        start = 1234 if i<10 else 123
        for j in range(start, 10000/i):
            r = i*j
            # if IP(reduce(op.add, map(str, [i, j, r]))):
            if IP(str(i)+str(j)+str(r)):
                p.add(r)
    print "Result: {}".format(sum(p))

if __name__ == "__main__":
    bruteForce()
    newBruteForce()
