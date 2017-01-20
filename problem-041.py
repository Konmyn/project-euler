#!/usr/bin/python
# -*- coding: utf-8 -*-


import random
from itertools import permutations

def miller_rabin(n, k=20):
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

def concatenate_tuple(num_tuple):
    number = 0
    for n in num_tuple:
        number = number*10 + n
    return number

def main():
    findit = False
    for limit in range(3, 11)[::-1]:
        perm = permutations(range(1, limit)[::-1])
        while True:
            try:
                num = concatenate_tuple(perm.next())
                if miller_rabin(num):
                    findit = True
                    break
            except StopIteration:
                break
        if findit == True:
            break
    print "Result: {}".format(num)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
