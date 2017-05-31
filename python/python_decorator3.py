#!/usr/bin/python
# -*- coding: utf-8 -*-


from timeit import default_timer


def rtime(params):
    def runtime(func):
        def new_func(*args, **kwargs):
            print "Running {}".format(func.__name__)
            start_time = default_timer()
            print('parameters go here: {}'.format(params))
            result = func(*args, **kwargs)
            during = default_timer() - start_time
            print "Time used(s): {}".format(during)
            return result
        return new_func
    return runtime


@rtime('HAHAHA')
def brute_force_method(uplimit):
    total = 0
    for n in xrange(1, uplimit):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    print "Result: {}".format(total)


if __name__ == "__main__":
    uplimit = 10**4
    brute_force_method(uplimit)
