#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_both_palindromic(natural):
    str_n = str(natural)
    if str_n == str_n[::-1]:
        bin_str_n = bin(natural)[2:]
        if bin_str_n == bin_str_n[::-1]:
            return True
    return False


def main():
    number = 1
    total_sum = 0
    while number<10**6:
        if is_both_palindromic(number):
            total_sum += number
        number += 1
    print "Result: {}".format(total_sum)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
