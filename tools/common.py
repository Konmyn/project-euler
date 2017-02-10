#!/usr/bin/python
# -*- coding: utf-8 -*-


import operator as op
from math import sqrt
from math import factorial as ft


# fast easy reading by string and list method.
def is_palindromic(n):
    # # data type check if necessary
    # if not isinstance(n, int) or n<0:
    #     raise TypeError
    n = str(n)
    return n == n[::- 1]

# check if n is pandigital or not.
# We shall say that an n-digit number is pandigital
# if it makes use of all the digits 1 to n exactly once
def is_pandigital(n, s=9):
    n=str(n);
    return len(n)==s and not '1234567890'[:s].strip(n)

# from math import factorial
# or you can do above if you want:)
def factorial(n): return reduce(op.mul, xrange(1, n+1), 1)

# A positive proper divisor is a positive divisor of a number n, excluding n itself.
# For example, 1, 2, and 3 are positive proper divisors of 6, but 6 itself is not.
def proper_divisors_sum(n):
    s, t = 1, sqrt(n)
    for i in xrange(2, int(t)+1):
        if n%i == 0:
            s += i + n/i
    if t == int(t): s -= int(t)
    return s

# https://en.wikipedia.org/wiki/Permutation
# permutations count from zero.
# return the (n-1)th permutation of string s.
def permutation(n, s):
   if len(s)==1: return s
   q, r = divmod(n, ft(len(s)-1))
   return s[q] + permutation(r, s[:q] + s[q+1:])

def DigitsPowerSum(n, exp):
    dps = 0
    while n:
        dps, n = dps+(n%10)**exp, n/10
    return dps

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

# this function is based on the defination of prime.
def is_prime(n):
    """Returns True if n is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    # a prime (except 2 and 3) is of form 6k - 1 or 6k + 1
    while i * i <= n:
        if not n % i or not n % (i + 2):
            return False
        i += 6
    return True

# below method seems slightly different but is no faster.
# def is_prime(n):
#     if n <= 1: return False
#     if n <= 3: return True
#     if n%2==0 or n%3 == 0: return False
#     r = int(sqrt(n))
#     f = 5
#     while f <= r:
#         if n%f == 0 or n%(f+2) == 0: return False
#         f+= 6
#     return True

