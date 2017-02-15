#!/usr/bin/python
# -*- coding: utf-8 -*-


from operator import add
from tools.runningTime import runTime


# (a+b) % n = ((a%n) + (b%n)) % n
@runTime
def bruteForce(L=1000):
    dl = 10**10
    result = sum([pow(i, i)%(dl) for i in xrange(1, L+1)])%dl
    print "Result: {}".format(result)

@runTime
def newBruteForce(L=1000):
    dl = 10**10
    result = sum([pow(i, i) for i in xrange(1, L+1)])%dl
    print "Result: {}".format(result)

if __name__ == "__main__":
    bruteForce()
    newBruteForce()
