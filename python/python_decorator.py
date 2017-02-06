#!/usr/bin/python
# -*- coding: utf-8 -*-


from timeit import default_timer


# class as decorator
class runTime(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print "Running {}".format(self.func.__name__)
        start_time = default_timer()
        self.func()
        end_time = default_timer()
        print "Time used(s): {}".format(end_time-start_time)

# function as decorator
def runtime(func):
    def new_func():
        print "Running {}".format(new_func.__name__)
        start_time = default_timer()
        func()
        end_time = default_timer()
        print "Time used(s): {}".format(end_time-start_time)
    new_func.__name__ = func.__name__
    return new_func

uplimit = 10**7

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
