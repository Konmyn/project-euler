#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import prime_sieve
from math import log


# find the max power of primes in each number.
@runTime
def least_common_multiple(limit = 20):
    primes = prime_sieve(limit+1)
    result = reduce(lambda x, y : x*y,
           (pow(i, int(log(limit, i))) if i*i<limit else i for i in primes), 1)
    print "Result: {}".format(result)


if __name__ == "__main__":
    least_common_multiple()
