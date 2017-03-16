#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import is_prime, prime_sieve


@runTime
def bruteForce(L=10**8+1):
    primes = prime_sieve(L)
    p_set = set(primes)
    s_n = 0
    for n in xrange(2,L):
        if n in p_set:
            s_n += n
            continue
        cache = {}
        for p in primes:
            if p>n:
                break
            if n%p == 0:
                cache[p], n = 1, n/p
                while n%p == 0:
                    cache[p], n = cache[p]+1, n/p
        maxn = 0
        for k, v in cache.iteritems():
            m = k*v
            if v == 1:
                maxn = max(maxn, m)
                continue
            tm, tk, tv = m, k, 99999
            while tv>=v:
                tm, tk, tv = tm-k, k, 0
                while tm>=tk:
                    tv += tm/tk
                    tk *= k
            maxn = max(maxn, tm+k)
        s_n += maxn
    print "Result: {}".format(s_n)


if __name__ == "__main__":
    bruteForce(100001)
