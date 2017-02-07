#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


# including the end point, so stop+1.
def sum_of_square(stop, start=1, step=1):
    return reduce(lambda x, y: x + y ** 2, xrange(start, stop + 1, step), 0)


def square_of_sum(stop, start=1, step=1):
    # simple and stupid
    return pow(sum(xrange(start, stop + 1, step)), 2)

# try to find formula next time! this one is stupid
@runTime
def normal_method(stop=100):
    diff = square_of_sum(stop) - sum_of_square(stop)
    print "Result: {}".format(diff)

@runTime
def by_formula(stop=100):
    result = stop*(stop-1)*(stop+1)*(3*stop+2)/12
    print "Result: {}".format(result)


if __name__ == "__main__":
    normal_method()
    by_formula()
