#!/usr/bin/python
# -*- coding: utf-8 -*-


import random
from itertools import combinations


def is_prime(n):
    i = 5
    while i * i <= n:
        if not n % i or not n % (i + 2):
            return False
        i += 6
    return True


def by_defination_check(n, one, times):
    i = j = 1
    while i < times:
        if is_prime(n + one * i):
            j += 1
        if j > 7:
            return True
        if i - j > times -8:
            return False
        i += 1
    return False


def miller_rabin(n, k=40):
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in xrange(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in xrange(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def digits_list(n):
    n //= 10
    digits = []
    while n:
        digits.append(n%10)
        n //= 10
    return digits


def has_duplicate_digits(n):
    digits = digits_list(n)
    x_0 = digits.count(0)
    y_1 = digits.count(1)
    z_2 = digits.count(2)
    prepare = []
    if x_0 < 2 and y_1 < 2 and z_2 < 2:
        return False
    if x_0 > 1:
        prepare.append(all_factors(digits, 0, x_0))
    if y_1 > 1:
        prepare.append(all_factors(digits, 1, y_1))
    if z_2 > 1:
        prepare.append(all_factors(digits, 2, z_2))
    return prepare


def all_factors(digits, digit, counts):
    n = 10
    factors = []
    candi = []
    for i in digits:
        if i == digit:
            factors.append(n)
        n *= 10
    i = 2
    while i <= counts:
        for j in combinations(factors, i):
            candi.append(sum(j))
        i += 1
    return [10 - digit, candi]


def is_prime_family(n, lists):
    for one in lists[1]:
        times = 1
        count_pass = 1
        while times < lists[0]:
            if miller_rabin(n + (one * times)):
                count_pass += 1
            if count_pass > 7:
                if by_defination_check(n, one, lists[0]):
                    return True
            if times - count_pass > lists[0] - 8:
                break
            times += 1
    return False


def main():
    # there are about 5096876 primes in 8 digits number.
    # 101 % 6 = 5
    n = 101
    step = 2
    while True:
        if miller_rabin(n, 3):
            ones = has_duplicate_digits(n)
            if ones:
                for one in ones:
                    if is_prime_family(n, one):
                        print "Result: {}".format(n)
                        return
        n += step
        step = 6 - step


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
