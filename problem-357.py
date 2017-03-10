#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import is_prime, prime_sieve


@runTime
def bruteForce(L=100000001):
    targets = [2]
    primes = set([2, 3])
    for n in xrange(4, L, 2):
        if is_prime(n+1):
            primes.add(n+1)
            for i in (2, int(n**0.5)):
                if n%i == 0 and i+n/i not in primes:
                    break
            else:
                targets.append(n)
    print targets
    print "Result: {}".format(sum(targets))

@runTime
def newBruteForce(L=100000001):
    primes = prime_sieve(L)
    pset = set(primes)
    targets = []
    for p in primes:
        t = p-1
        for n in range(2, int(t**0.5)):
            if t%n==0 and n+t/n not in pset:
                break
        else:
            targets.append(t)
    print targets
    print "Result: {}".format(sum(targets))


if __name__ == "__main__":
    L = 10001
    bruteForce(L)
    newBruteForce(L)
