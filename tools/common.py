#!/usr/bin/python
# -*- coding: utf-8 -*-


# fast easy reading by string and list method.
def is_palindromic(n):
    # # data type check if necessary
    # if not isinstance(n, int) or n<0:
    #     raise TypeError
    n = str(n)
    return n == n[::- 1]

def prime_sieve(n):
    """
    Return a list of prime numbers from 2 to a prime < n. Very fast (n<10,000,000) in 0.4 sec.

    Example:
    >>>prime_sieve(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]

    Algorithm & Python source: Robert William Hanks
    http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/18944432#18944432
    """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]
