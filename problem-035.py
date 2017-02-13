#!/usr/bin/python
# -*- coding: utf-8 -*-


from re import search
from tools.runningTime import runTime
from tools.common import is_prime, prime_sieve


def rotate_list(number):
    length = len(str(number)) - 1
    num_list = []
    for i in xrange(length):
        number = number%10*10**(length)+number//10
        num_list.append(number)
    return num_list

@runTime
def bruteForce(uplimit=10**6):
    rotate_prime = set([2, 3, 5, 7])
    for natural in xrange(11, uplimit, 2):
        if natural not in rotate_prime and is_prime(natural):
            n_list = rotate_list(natural)
            if all(map(is_prime, n_list)):
            # flag = True
            # for n in n_list:
            #     if not is_prime(n):
            #         flag = False
            #         break
            # if flag:
                rotate_prime.update([natural]+n_list)
                # for n in n_list:
                #     rotate_prime.add(n)
    print rotate_prime
    print "Result: {}".format(len(rotate_prime))

# return a list containing its left-rotate for str(number)
def rotate(s):
    return[s[n:]+s[:n] for n in range(1, len(s))]

# Circular primes (numbers that remain prime under cyclic shifts of digits).
# https://oeis.org/A016114
@runTime
def newBruteForce(L=10**6):
    primes = set(['2', '5']+[str(p) for p in prime_sieve(L) if not search('024568', str(p))])
    counter = sum(all(n in primes for n in rotate(p)) for p in primes)
    print "Result: {}".format(counter)


if __name__ == "__main__":
    bruteForce()
    newBruteForce()
