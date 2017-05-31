#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import time


fib = {0: 0, 1: 1}


# in python, recursion is limited to 999 calls.
def fibonacci(n):
    if n >= sys.getrecursionlimit():
        print('Maximum recursion depth exceeded.')
        return
    if n not in fib:
        fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib[n]


def fibona(n):
    fiba, fibb = 0, 1
    for i in range(n - 1):
        fiba, fibb = fibb, fiba + fibb
    return fibb


if __name__ == '__main__':
    num = 999
    start = time.time()
    print(fibonacci(num))
    print('time used: {}'.format(time.time() - start))
    start = time.time()
    print(fibona(num))
    print('time used: {}'.format(time.time() - start))
