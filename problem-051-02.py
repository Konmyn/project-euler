#!/usr/bin/python
# -*- coding: utf-8 -*-


import random


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
    digits = digits[::-1]
    return digits


def is_prime_family(n, digits):
    if 0 in digits:
        if total_replace_test(n, 0):
            return True
        if digits[0] > 2:
            if part_replace_test(n, 0):
                return True
    if 1 in digits and digits['end_with_1']:
        if total_replace_test(n, 1, True):
            return True
        if digits[1] > 2:
            if part_replace_test(n, 1, True):
                return True
    if 1 in digits and not digits['end_with_1']:
        if total_replace_test(n, 1):
            return True
        if digits[1] > 2:
            if part_replace_test(n, 1):
                return True
    if 2 in digits:
        if total_replace_test(n, 2):
            return True
        if digits[2] > 2:
            if part_replace_test(n, 2):
                return True
    return False


def has_duplicate_digits(n):
    digits_count = {'is_p': False, 'end_with_1': False}
    n = str(n)
    x = n.count('0')
    if n[-1] == '1':
        digits_count['end_with_1'] = True
        y = n.count('1') - 1
    else:
        y = n.count('1')
    z = n.count('2')
    if x > 1:
        digits_count['is_p'] = True
        digits_count[0] = x
    if y > 1:
        digits_count['is_p'] = True
        digits_count[1] = y
    if z > 1:
        digits_count['is_p'] = True
        digits_count[2] = z
    return digits_count


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
