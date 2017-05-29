#!/usr/bin/python
# -*- coding: utf-8 -*-


from timeit import default_timer
from functools import wraps


def logger(func):
    import logging
    logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, kwargs: {}'.format(args, kwargs))
        return func(*args, **kwargs)
    return wrapper


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


@logger
@runtime
def brute_force_method(uplimit):
    total = 0
    for n in xrange(1, uplimit):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    print "Result: {}".format(total)


if __name__ == "__main__":
    uplimit = 10**7
    brute_force_method(uplimit)
