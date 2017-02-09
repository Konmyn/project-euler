#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import prime_sieve


def decimal_str(denominator):
    dec_str = '0.'
    nominator = 10
    while nominator != 0 or len(dec_str) < 50:
        dec_str += str(nominator//denominator)
        nominator = nominator%denominator*10
    return dec_str

def recurring_cycle(denominator):
    nomi_list = [10]
    nominator = 10
    while True:
        nominator = nominator%denominator*10
        if nominator == 0:
            return 0
        elif nominator in nomi_list:
            return len(nomi_list[nomi_list.index(nominator):])
        nomi_list.append(nominator)

@runTime
def brute_force_method(Limit=1000):
    max_len = 0
    for n in xrange(1, Limit):
        if recurring_cycle(n) > max_len:
            max_len, d = recurring_cycle(n), n
    print "Result: {}, Length: {}".format(d, max_len)

@runTime
def improved(Limit=1000):
    if Limit<8: return 3
    primes = prime_sieve(Limit)[::-1]
    for p in primes:
        if recurring_cycle(p) == p-1:
            print "Result: {}".format(p)
            return

# Fermat’s little theorem
# https://en.wikipedia.org/wiki/Fermat's_little_theorem
# Full reptend primes: primes with primitive root 10.
# https://oeis.org/A001913
@runTime
def by_formula(Limit=1000):
    if Limit<8: return 3
    primes = prime_sieve(Limit)[::-1]
    for p in primes:
        period = 1
        # not recommend like this:
        # while (pow(10, c) - 1) % p != 0:
        while pow(10, period, p) != 1: period += 1
        if p-1 == period: break
    print "Result: {}".format(p)


if __name__ == "__main__":
    L=2000
    brute_force_method(L)
    improved(L)
    by_formula(L)
