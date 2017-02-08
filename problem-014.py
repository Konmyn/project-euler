#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


def chain_length(number):
    length = 1
    while number != 1:
        if number % 2:
            number = 3 * number + 1
            length += 1
        else:
            number /= 2
            length += 1
    return length

@runTime
def brute_force_method(limit=10**6):
    max_length = 0
    for n in xrange(1, limit):
        length = chain_length(n)
        if length > max_length:
            max_length = length
            target = n
    print "Result: {} has longest chain {}".format(target, max_length)


if __name__ == "__main__":
    brute_force_method()
