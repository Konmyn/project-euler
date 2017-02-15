#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import is_prime


def fit_conjecture(n_odd):
    n, pt = 1, 2
    while pt<n_odd:
        if is_prime(n_odd-pt):
            return True
        n, pt = n+1, pt+4*n+2
    return False

@runTime
def bruteForce():
    odd = 33
    while True:
        odd += 2
        if is_prime(odd) or fit_conjecture(odd):
            continue
        print "Result: {}".format(odd)
        break

@runTime
def newBruteForce():
    n = 5
    primes = set([2, 3])
    while True:
        if all(n%p for p in primes):
            primes.add(n)
        elif not any((n-2*i*i) in primes for i in range(1, int(n**0.5)+1)):
            break
        n += 2
    print "Result: {}".format(n)


if __name__ == "__main__":
    bruteForce()
    newBruteForce()
