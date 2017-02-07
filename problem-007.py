#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import prime_sieve
from math import log


def primes_dict(counts):
    _key = 1
    primes = {_key: 2}
    if not isinstance(counts, int):
        return {}
    if counts < 1:
        return {}
    if counts == 1:
        return primes
    n = 3
    _key += 1
    _is_prime = True
    while _key <= counts:
        for v in primes.itervalues():
            if not n % v:
                _is_prime = False
                break
        if _is_prime:
            primes[_key] = n
            _key += 1
        n += 2
        _is_prime = True
    return primes

@runTime
def brute_force_method(counts=10001):
    the_prime = primes_dict(counts)
    print "Result: {}".format(the_prime[counts])

# inverse of the Prime Counting Function, it is just generates a good guess.
# http://mathworld.wolfram.com/PrimeCountingFunction.html
def get_uplimit(counts):
    n = 2
    while 1.25*n/log(n)<counts:
        n *= 2
    return n + 100

@runTime
def fast_prime_sieve(counts=10001):
    primes = prime_sieve(get_uplimit(counts))
    print "Result: {}".format(primes[counts-1])

if __name__ == "__main__":
    brute_force_method()
    fast_prime_sieve(100001)
