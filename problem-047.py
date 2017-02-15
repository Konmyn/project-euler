#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import is_prime, factor


PRIME_LIST = []

def prime_factor_counter(number):
    if is_prime(number):
        PRIME_LIST.append(number)
        return 1
    counter = 0
    for p in PRIME_LIST:
        if number%p == 0:
            counter += 1
            while number%p==0:
                number //= p
        if number == 1:
            break
    return counter

# this method cost 10 times more than above.
def primeFactorCounter(n):
    cache = n
    counter = 0
    if n%2==0:
        counter += 1
        while n%2==0:
            n /= 2
    f = 3
    while f<=n:
        if n%f==0:
            counter += 1
            while n%f==0:
                n /= f
        f += 2
    return counter

@runTime
def bruteForce():
    # number must start within 2, becasue PRIME_LIST need them.
    number, counter = 1, 0
    while counter < 4:
        number += 1
        if prime_factor_counter(number) > 3:
        # if primeFactorCounter(number) > 3:
            counter += 1
        else:
            counter = 0
    # print PRIME_LIST
    print "Result: {}".format(number-3)

@runTime
def newBruteForce():
    ci = 0
    nf = 4      # number of distinct factors
    ns = 4      # number of consecutive integers
    n = 2*3*5*7 # starting candidate for search
    while ci != ns:
        n += 1
        if len(factor(n)) == nf:
            ci += 1
        else:
            ci = 0
    print "Result: {}".format(n-nf+1)


if __name__ == "__main__":
    # bruteForce()
    newBruteForce()
