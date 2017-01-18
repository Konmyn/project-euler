#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    product = reduce(lambda x, y: x*y, range(1, 101))
    the_sum = 0
    while product:
        the_sum += product%10
        product //= 10
    print "Result: {}".format(the_sum)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
