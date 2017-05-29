#!/usr/bin/python
# -*- coding: utf-8 -*-


from timeit import default_timer
from functools import wraps, update_wrapper


# class as decorator
# suggestion: better to use function as decorator.
class runTime(object):
    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        print "Running {}".format(self.func.__name__)
        start_time = default_timer()
        result = self.func(*args, **kwargs)
        during = default_timer() - start_time
        print "Time used(s): {}".format(during)
        return result


# function as decorator
def runtime(func):

    @wraps(func)
    def new_func(*args, **kwargs):
        print "Running {}".format(new_func.__name__)
        start_time = default_timer()
        result = func(*args, **kwargs)
        during = default_timer() - start_time
        print "Time used(s): {}".format(during)
        return result
    return new_func


# annotation can be inserted between decorator and its function.
# this method time cost should be O(n).
@runtime
def brute_force_method(uplimit):
    total = 0
    for n in xrange(1, uplimit):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    print "Result: {}".format(total)


# this method time cost should be O(1).
@runTime
def formula_method(uplimit):
    count_3 = uplimit // 3
    count_5 = uplimit // 5
    count_15 = uplimit // 15
    total = (count_3 * (count_3 + 1) * 3 + count_5 * (count_5 + 1) * 5 -
             count_15 * (count_15 + 1) * 15) // 2
    print "Result: {}".format(total)


if __name__ == "__main__":
    uplimit = 10**7
    brute_force_method(uplimit)
    formula_method(uplimit)
