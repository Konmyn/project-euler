#!/usr/bin/python
# -*- coding: utf-8 -*-


import time
import multiprocessing


def summod(n):
    result = 0
    for i in xrange(n):
        result += i
        result %= 100
    return result

start = time.time()
p = multiprocessing.Pool()
result = p.map(summod, xrange(10**4))
p.close()
p.join()
print('Pool took: {}'.format(time.time() - start))

start = time.time()
result = list()
for i in xrange(10**4):
    result.append(summod(i))
print('Serial took: {}'.format(time.time() - start))
