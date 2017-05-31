#!/usr/bin/python
# -*- coding: utf-8 -*-


import time


def countdown(n):
    while n>0:
        n -= 1

COUNT = 10**8

start = time.time()
countdown(COUNT)
print(time.time() - start)
