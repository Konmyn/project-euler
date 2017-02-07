#!/usr/bin/python
# -*- coding: utf-8 -*-


from timeit import default_timer


# class as decorator
class runTime(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *arg):
        print 'Running "{}"'.format(self.func.__name__)
        start_time = default_timer()
        self.func(*arg)
        end_time = default_timer()
        print "Time used(s): {}".format(end_time-start_time)

# function as decorator
def runtime(func):
    def new_func(*arg):
        print 'Running "{}"'.format(new_func.__name__)
        start_time = default_timer()
        func(*arg)
        end_time = default_timer()
        print "Time used(s): {}".format(end_time-start_time)
    new_func.__name__ = func.__name__
    return new_func
