#!/usr/bin/python
# -*- coding: utf-8 -*-


import time


def calc_square(nlist):
    print('calculate squares')
    for n in nlist:
        time.sleep(0.2)
        print('square: {}'.format(n * n))


def calc_cube(nlist):
    print('calculate cubes')
    for n in nlist:
        time.sleep(0.2)
        print('cube: {}'.format(n * n * n))

arr = range(10)

start = time.time()
calc_square(arr)
calc_cube(arr)
print('Done in {} seconds'.format(time.time() - start))
