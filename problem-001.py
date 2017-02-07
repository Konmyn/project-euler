#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


uplimit = 10**3

@runTime
# annotation can be inserted between decorator and its function.
# this method time cost should be O(n).
def brute_force_method():
    global uplimit
    total = 0
    for n in xrange(1, uplimit):
        if n%3 == 0 or n%5 == 0:
            total += n
    print "Result: {}".format(total)

# return the sum of numbers '<=' limit that are divisible by number.
def sum_num(limit, number):
    limit //= number
    return number*limit*(limit+1) // 2

@runTime
# this method time cost should be O(1).
# see Inclusion–exclusion principle on Wiki.
def formula_method():
    global uplimit
    total = sum_num(uplimit-1, 3) + sum_num(uplimit-1, 5) -\
            sum_num(uplimit-1, 3*5)
    print "Result: {}".format(total)


if __name__ == "__main__":
    brute_force_method()
    formula_method()
