#!/usr/bin/python
# -*- coding: utf-8 -*-


import time
import multiprocessing


square_list, cube_list = list(), list()


def calc_square(nlist):
    global square_list
    print('calculate squares')
    for n in nlist:
        time.sleep(0.2)
        print('square: {}'.format(n * n))
        square_list.append(n * n)


def calc_cube(nlist):
    global cube_list
    print('calculate cubes')
    for n in nlist:
        time.sleep(0.2)
        print('cube: {}'.format(n * n * n))
        cube_list.append(n * n * n)

arr = range(10)

start = time.time()
t1 = multiprocessing.Process(target=calc_square, args=(arr,))
t2 = multiprocessing.Process(target=calc_cube, args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
# below is not right because it's need interprocess communication (IPC)
# to share data between two process
print('square result: {}\ncube result: {}'.format(square_list, cube_list))
print('Done in {} seconds'.format(time.time() - start))
