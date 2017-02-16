#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import prime_sieve, is_prime


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
    prime_sum = [0]
    for p in prime_sieve(L/100):
        prime_sum.append(prime_sum[-1]+p)
        if prime_sum[-1] >= L:
            break
    c = len(prime_sum)

    terms = 1
    for i in xrange(c):
        for j in xrange(c-1, i+terms, -1):
            n = prime_sum[j] - prime_sum[i]
            if j-i > terms and is_prime(n):
                terms, max_prime = j-i, n
                break

    print "Result: max prime {} with {} terms".format(max_prime, terms)


if __name__ == "__main__":
    bruteForce()
    newBruteForce()
