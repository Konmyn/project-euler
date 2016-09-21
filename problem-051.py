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


def is_prime_family(n):
    x = str(n).count('0')
    y = str(n).count('1')
    z = str(n).count('2')
    if x < 2 and y < 2 and z < 2:
        return False
    count_fail = 0
    count_succe = 1
    if x >= 2:
        for i in range(1, 10):
            if miller_rabin(int(str(n).replace('0', '{}'.format(i)))):
                count_succe += 1
                continue
            count_fail += 1
            if count_fail > 2:
                break
    if count_succe >= 8:
        return True
    count_fail = 0
    count_succe = 1
    if y >= 2:
        for i in range(2, 10):
            if miller_rabin(int(str(n).replace('1', '{}'.format(i)))):
                count_succe += 1
                continue
            count_fail += 1
            if count_fail > 1:
                break
    if count_succe >= 8:
        return True
    count_fail = 0
    count_succe = 1
    if z >= 2:
        for i in range(3, 10):
            if miller_rabin(int(str(n).replace('2', '{}'.format(i)))):
                count_succe += 1
                continue
            count_fail += 1
            if count_fail > 0:
                break
    if count_succe >= 8:
        return True
    return False



def main():
    # there are about 5096876 primes in 8 digits number.
    # 10000001 % 6 = 5
    n = 10000001
    count = 0
    result = False
    while n < 20000000:
        if miller_rabin(n, 3):
            result = is_prime_family(n)
        if result:
            result = n
            break
        if miller_rabin(n + 2, 3):
            count += 1
        if result:
            result = n
            break
        n += 6
    print "Result: {}".format(result)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
