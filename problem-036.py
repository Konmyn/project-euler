#!/usr/bin/python
# -*- coding: utf-8 -*-


import itertools
from tools.runningTime import runTime
from tools.common import is_palindromic


def is_both_palindromic(natural):
    str_n = str(natural)
    if str_n == str_n[::-1]:
        bin_str_n = bin(natural)[2:]
        return bin_str_n == bin_str_n[::-1]
    return False

@runTime
def bruteForce(L=10**6):
    total_sum = 0
    for number in xrange(1, L, 2):
        if is_both_palindromic(number):
            total_sum += number
    print "Result: {}".format(total_sum)

def pal_list(k):
    if k == 1:
        return [1, 3, 5, 7, 9]
    return [sum([n*(10**i) for i,n in enumerate(([x]+list(ys)+[z]+list(ys)[::-1]+[x]) if k%2
                                else ([x]+list(ys)+list(ys)[::-1]+[x]))])
            for x in xrange(1, 10, 2)    #check odd numbers only
            for ys in itertools.product(xrange(10), repeat=k/2-1)
            for z in (xrange(10) if k%2 else (None,))]

# do it myself first.
def pal_list_mine(k):
    x, y = range(1, 10, 2), range(10)
    if k == 1:
        return xrange(1, 10, 2)
    if k == 2:
        return [a*10**(k-1)+a for a in x]
    if k == 3:
        return [a*10**(k-1)+b*10**(k-2)+a for a in x for b in y]
    if k == 4:
        return [a*10**(k-1)+b*10**(k-2)+b*10**(k-3)+a for a in x for b in y]
    if k == 5:
        return [a*10**(k-1)+b*10**(k-2)+c*10**(k-3)+b*10**(k-4)+a for a in x for b in y for c in y]
    if k == 6:
        return [a*10**(k-1)+b*10**(k-2)+c*10**(k-3)+c*10**(k-4)+b*10**(k-5)+a for a in x for b in y for c in y]

# Numbers that are palindromic in bases 2 and 10.
# https://oeis.org/A007632
@runTime
def newBruteForce(L=6):
    s = 0
    for b in xrange(1, L+1):
        s += sum(n for n in pal_list(b) if is_palindromic(bin(n)[2:]))
        # s += sum(n for n in pal_list_mine(b) if is_palindromic(bin(n)[2:]))
    print "Result: {}".format(s)


if __name__ == "__main__":
    bruteForce()
    newBruteForce()
