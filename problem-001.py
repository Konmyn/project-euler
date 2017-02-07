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

@runTime
# this method time cost should be O(1).
def formula_method():
    global uplimit
    count_3 = uplimit//3
    count_5 = uplimit//5
    count_15 = uplimit//15
    total = (count_3*(count_3+1)*3 + count_5*(count_5+1)*5
             - count_15*(count_15+1)*15)//2
    print "Result: {}".format(total)


if __name__ == "__main__":
    brute_force_method()
    formula_method()
