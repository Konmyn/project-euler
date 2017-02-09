#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


def chain_length(number):
    length = 1
    f = lambda x: 3*x+1 if x%2 else x/2
    while number != 1:
        number = f(number)
        length += 1
    return length

@runTime
def brute_force_method(limit=10**6):
    print "Result: {}".format(max(xrange(1, limit), key=chain_length))

# Collatz sequence
# https://oeis.org/A006877
# https://en.wikipedia.org/wiki/Collatz_conjecture
c = [1, 2, 3, 6, 7, 9, 18, 19, 25, 27, 54, 55, 73, 97, 129, 171, 231, 235, 313, 327, 649, 654,
     655, 667, 703, 871, 1161, 2223, 2322, 2323, 2463, 2919, 3711, 6171, 10971, 13255, 17647,
     17673, 23529, 26623, 34239, 35497, 35655, 52527, 77031, 106239, 142587, 156159, 216367,
     230631, 410011, 511935, 626331, 837799, 1117065, 1126015, 1501353, 1564063, 1723519,
     2298025, 3064033, 3542887, 3732423, 5649499, 6649279, 8400511, 11200681]

@runTime
def somehow_cheating(limit=10**6):
    if limit>c[-1]:
        print "Result: out of my power."
        return
    print "Result: {}".format(min(c[::-1], key=lambda x: x>limit))

@runTime
def hailstone_generator(limit=10**6):
    hailstone = lambda n: 3*n + 1 if n%2 else n//2

    def d(n, cache={1:1}):
        if n not in cache: cache[n] = d(hailstone(n)) + 1
        return cache[n]

    print "Result: {}".format(max(xrange(1, limit), key=d))


if __name__ == "__main__":
    brute_force_method()
    somehow_cheating()
    hailstone_generator()
