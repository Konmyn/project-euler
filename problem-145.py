#!/usr/bin/python
# -*- coding: utf-8 -*-


def reverse_number(n):
    m = 0
    while n:
        m = m * 10 + n % 10
        n //= 10
    return m


def is_reversible(n):
    sum_n = n + int(str(n)[::-1])
    while sum_n:
        if not sum_n % 10 % 2:
            return False
        sum_n //= 10
    return True


def filter_number(n):
    str_n = str(n)
    if str_n < str_n[::-1]:
        return True
    return False


def main():
    count = 0
    n = 12
    stop = 1000000000
    while n < stop:
        if filter_number(n):
            if is_reversible(n):
                count += 1
        n += 1
    print "Result: {}".format(count * 2)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)

# Result: 608720
# Time used(s): 1333.83219504
