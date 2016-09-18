#!/usr/bin/python
# -*- coding: utf-8 -*-


# including the end point, so stop+1.
def sum_of_square(stop, start=1, step=1):
    return reduce(lambda x, y: x + y ** 2, xrange(start, stop + 1, step), 0)


def square_of_sum(stop, start=1, step=1):
    return pow(sum(xrange(start, stop + 1, step)), 2)


def main():
    stop = 100
    diff = square_of_sum(stop) - sum_of_square(stop)
    print "Result: {}".format(diff)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
