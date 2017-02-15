#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import prime_sieve


@runTime
def bruteForce(L=10**6):
    primes = prime_sieve(L)
    i = 1
    while sum(primes[:i]) < L:
        i += 1
    i -= 1
    max_possible = i
    _loop = True
    while _loop:
        j = 0
        while j <= (max_possible - i):
            if sum(primes[j:j + i]) in primes:
                _loop = False
                break
            j += 1
        i -= 1
    i += 1
    print "Result: {}".format(sum(primes[j:j + i]))

# Prime Sums
# http://mathworld.wolfram.com/PrimeSums.html
@runTime
def newBruteForce(L=10**6):


if __name__ == "__main__":
    bruteForce()
