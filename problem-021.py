#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import proper_divisors_sum as ps


def divisor_sum(number):
    divisor, divisors = 2, set([1])
    while divisor*divisor <= number:
        if not number % divisor:
            divisors.add(divisor)
            divisors.add(number / divisor)
        divisor += 1
    return sum(divisors)

@runTime
def brute_force_method(limit=10000):
    amicable = []
    for natural in range(2, limit):
        if divisor_sum(divisor_sum(natural)) == natural and\
           divisor_sum(natural) != natural:
            amicable.append(natural)
    print "Result: {}".format(sum(amicable))

@runTime
def amicable_sum(L=10000):
    s = 0
    for i in xrange(2, L):
        ds = ps(i)
        if ds>i and ps(ds)==i: s += ds+i
    print "Result: {}".format(s)


if __name__ == "__main__":
    brute_force_method()
    amicable_sum()
