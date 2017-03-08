#!/usr/bin/python
# -*- coding: utf-8 -*-


from itertools import permutations
from tools.runningTime import runTime
from tools.common import prime_sieve, is_prime


@runTime
def setIntersection(L=10000, size=5):
    primes = prime_sieve(L)
    print "Result: {}".format()


if __name__ == "__main__":
    bruteForce()
