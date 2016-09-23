#!/usr/bin/python
# -*- coding: utf-8 -*-


import random


def is_prime(n):
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


def t(n):
    return 2 * n ** 2 - 1


def main():
    n = 2
    stop = 50000000
    count = 0
    while n <= stop:
        if miller_rabin(t(n), 3):
            count += 1
        n += 1
    print "Result: {}".format(count)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)

# Result: 5437849
# Time used(s): 1290.86269307
