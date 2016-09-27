#!/usr/bin/python
# -*- coding: utf-8 -*-


def f(n):
    digits = digit_list(n)
    start = start_number(n)
    for x in start:
        sec_list = gener_number(x[0], digits[1], n)


def digit_list(n):
    digits = list()
    while n:
        digits.append(n % 10)
        n //= 10
    return digits


def start_number(target=0):
    digits = digit_list(target)
    n = 0
    cand = []
    while n < 10:
        if (n * digits[0]) % 10 < 3:
            cand.append([n, digit_list(n * target)])
        n += 1
    return cand


def gener_number(i, digits=0, target=0):
    n = 0
    cand = []
    while n < 10:
        if (n * digits + target[1]) % 10 < 3:
            cand.append((n, (n * digits + target[1]) // 10))
        n += 1
    return cand


def digits_check(n):
    while n:
        if n % 10 > 2:
            return False
        n //= 10
    return True


def main():
    n = 1
    stop = 100
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
