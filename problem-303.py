#!/usr/bin/python
# -*- coding: utf-8 -*-


def f(n):
    multiple = 1
    while True:
        if digits_check(multiple*n):
            return multiple     # note the return value.
        multiple += 1


def digits_check(n):
    while n:
        if n % 10 > 2:
            return False
        n //= 10
    return True


def main():
    n = 1
    stop = 10000
    sum_all = 0
    while n <= stop:
        sum_all += f(n)
        n += 1
        if not n % 200:
            print n
    print "Result: {}".format(sum_all)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
