#!/usr/bin/python
# -*- coding: utf-8 -*-


import random
from itertools import combinations

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
    digits = []
    while n:
        digits.append(n%10)
        n //= 10
    return digits


def is_prime_family(n, digits):
    return False


def has_duplicate_digits(n):
    digits = digits_list(n)
    x_0 = digits.count(0)
    y_1 = digits[:-1].count(1)
    z_2 = digits.count(2)
    if x_0 < 2 or y_1 < 2 or z_2 < 2:
        return False
    result = all_calc(digits, x_0, y_1, z_2)
    return result


def all_calc(digits, x=0, y=0, z=0):
    cal_list = []
    list_0 = []
    list_1 = []
    list_2 = []
    if x > 1:
        list_0.append(9)
        list_0.append([replace_all(digits, 0)])
        if x > 2:
            list_0[1] += replace_2digits(digits, 0)
            if x > 3:
                pass
                if x > 4:
                    pass
                    if x > 5:
                        pass
        cal_list.append(list_0)
    if y > 1:
        list_1.append(8)
        list_1.append([replace_all(digits, 1)])
        if x > 2:
            list_1[1] += replace_2digits(digits, 1)
            if x > 3:
                pass
                if x > 4:
                    pass
                    if x > 5:
                        pass
                        if x > 6:
                            pass
        cal_list.append(list_1)
    if z > 1:
        list_2.append(7)
        list_2.append([replace_all(digits, 2)])
        if x > 2:
            list_2[1] += replace_2digits(digits, 2)
            if x > 3:
                pass
                if x > 4:
                    pass
                    if x > 5:
                        pass
                        if x > 6:
                            pass
        cal_list.append(list_2)


def all_factors(lists, digits):
    n = 10
    factors = []
    for i in lists[1:]:
        if i == digits:
            factors.append(n)
        n *= 10
    count = 2
    while count < len(factors):

        count += 1
    return factors


def replace_2digits(lists, digits, count):
    n = 0
    for i in lists:


def main():
    # there are about 5096876 primes in 8 digits number.
    # 10000001 % 6 = 5
    n = 10000001
    count = 0
    while n < 20000000:
        result = {'is_p': False, 'end_with_1': False}
        if miller_rabin(n, 3):
            result = has_duplicate_digits(n)
        if result['is_p']:
            if is_prime_family(n, result):
                result = n
                break
        result = {'is_p': False, 'end_with_1': False}
        if miller_rabin(n + 2, 3):
            result = has_duplicate_digits(n)
        if result['is_p']:
            if is_prime_family(n + 2, result):
                result = n + 2
                break
        n += 6
    print "Result: {}".format(result)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
