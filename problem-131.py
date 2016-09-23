#!/usr/bin/python
# -*- coding: utf-8 -*-


import random


def is_prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if not n % i or not n % (i + 2):
            return False
        i += 6
    return True


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


def is_perfect_cube(target, lower):
    n = lower + 1
    cuded = n ** 3
    while cuded <= target:
        if cuded == target:
            return True
        n += 1
        cuded = n ** 3
    return False


def prime_cube(p):
    n = 1
    while n <= p:
        cube = n ** 3 + n ** 2 * p
        if is_perfect_cube(cube, n):
            return True
        n += 1
    return False


def main():
    n = 2
    stop = 100
    count = 0
    while n < stop:
        if is_prime(n):
            if prime_cube(n):
                print n
                count += 1
        n += 1
    print "Result: {}".format(count)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
