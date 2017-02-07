#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


# kind of brute force method
@runTime
def divide_factors(target=600851475143):
    factor = 2
    while factor*factor <= target:
        if (target % factor == 0):
            target //= factor
        else:
            # after 2, consider only odd factors
            factor += 2 if factor>2 else 1
    print "Result: {}".format(target)


if __name__ == "__main__":
    divide_factors()
