#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    number = 2**1000
    digits_sum = 0
    while number:
        digits_sum += number % 10
        number //= 10
    print "Result: {}".format(digits_sum)

if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
