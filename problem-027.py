#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import prime_sieve, is_prime


@runTime
def bruteForce():
    record = {'a':0, 'b':0, 'len':0}
    for a in xrange(-999, 1000):
        for b in xrange(-1000, 1001):
            n = 0
            while is_prime(n*n+a*n+b):
                n += 1
            if n > record['len']:
                record.update({'a':a, 'b':b, 'len':n})
    print "Result: {}".format(record['a']*record['b'])

@runTime
def afterAnalysis():
    nmax = 0
    for b in prime_sieve(1001):
        for a in xrange(-b+2, 0, 2):
            n = 1
            while is_prime(n*n+a*n+b):
                n += 1
            if n>nmax:
                nmax, p = n, (a,b)
    print "Result: {}".format(p[0]*p[1])


if __name__ == "__main__":
    bruteForce()
    afterAnalysis()
