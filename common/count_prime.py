#!/usr/bin/python
# -*- coding: utf-8 -*-


# find specified counts of prime in a specified n.
def count_prime_single(n=1, prime=2):
    origin = n
    count = 0
    while not n % prime:
        count += 1
        n /= prime
    print "{} has '{}' {} in it as factors.".format(origin, count, prime)
    return count


def count_prime_single2(n=1, prime=2):
    origin = prime
    count = 0
    while not n % prime:
        count += 1
        prime *= origin
    print "{} has '{}' {} in it as factors.".format(n, count, origin)
    return count