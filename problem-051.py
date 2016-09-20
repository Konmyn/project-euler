#!/usr/bin/python
# -*- coding: utf-8 -*-


import random


def miller_rabin(n, k=40):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
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


def main():
    # there are about 5096876 primes in 8 digits number.
    # 10000001 % 6 = 5
    n = 10000001
    count = 0
    while n < 20000000:
        if miller_rabin(n, 3):
            count += 1
        if miller_rabin(n+2, 3):
            count += 1
        n += 6
    print "Result: {}".format(count)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
