#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_palindrome(number):
    str_num = str(number)
    half_len = len(str_num) / 2
    i = 0
    while i < half_len:
        if str_num[i] != str_num[- i - 1]:
            return False
        i += 1
    return True


# more easy reading using list method.
def is_palindrome2(number):
    str_num = str(number)
    if str_num != str_num[::- 1]:
            return False
    return True


# brute force
def main():
    _n = _m = _r = 0
    n = 999
    stop = 99
    while n > stop:
        m = n
        while m > stop:
            prod = m * n
            if is_palindrome(prod):
                if prod > _r:
                    _r = prod
                    _m = m
                    _n = m
            m -= 1
        n -= 1
    print "Result: {} * {} = {}".format(_m, _n, _r)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
