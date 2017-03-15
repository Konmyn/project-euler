#!/usr/bin/python
# -*- coding: utf-8 -*-


from math import log10
from tools.runningTime import runTime
from tools.common import is_prime, prime_sieve


@runTime
def bruteForce(L=10**14):
    d = range(10) # digits for loops
    a = range(1, 10) # start condition
    p = [1, 3, 7, 9] # primes end with these digits.
    s = 0 # the target sum
    loop = int(log10(L))-2 # no need for 1 digits and len(L-1) digits number
    for i in range(loop):
        c = []
        e = []
        for x in a:
            for y in d:
                n, m, q = x*10+y, y, x
                while q:
                    q, m = q//10, m+q%10
                q, r = divmod(n, m)
                if r==0:
                    c.append(n)
                    if is_prime(q):
                        e.append(n)
        a = c
        for x in e:
            for y in p:
                n = x*10+y
                if is_prime(n):
                    s += n
    print "Result: {}".format(s)


if __name__ == "__main__":
    bruteForce()
