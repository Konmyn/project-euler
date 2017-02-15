#!/usr/bin/python
# -*- coding: utf-8 -*-


from itertools import permutations
from tools.runningTime import runTime
from tools.common import is_prime, is_pandigital


@runTime
def byPermutation():
    np = set([2, 4, 5, 6, 8])
    # for expamle, 1->9 pandigital, its digits sum is 45,
    # which can be devide by 3, not prime of course.
    # so only 7, 4 pandigital is possible.
    for limit in [7, 4]:
        for perm in permutations(xrange(limit, 0, -1)):
            if perm[-1] in np:
                continue
            n = reduce(lambda x,y: 10*x+y, perm)
            # if miller_rabin(n):
            # double check, make it sure.
            if is_prime(n):
                print "Result: {}".format(n)
                return

@runTime
def newBruteForce():
    # write like this because we 'already' 'know' the result is 7 digits.
    n = 7654321
    while not (is_pandigital(n, 7) and is_prime(n)):
        n -= 2
    print "Result: {}".format(n)


if __name__ == "__main__":
    byPermutation()
    newBruteForce()
