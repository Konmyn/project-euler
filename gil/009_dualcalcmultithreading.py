#!/usr/bin/python
# -*- coding: utf-8 -*-


import time
import threading


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
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Done in {} seconds'.format(time.time() - start))
