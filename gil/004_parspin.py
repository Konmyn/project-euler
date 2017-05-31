#!/usr/bin/python
# -*- coding: utf-8 -*-


import time
from threading import Thread
from subprocess import Popen


def countdown(n):
    while n>0:
        n -= 1

# launch a useless process that spins
p = Popen(['python', '003_spin.py'])

COUNT = 10**8

t1 = Thread(target=countdown, args=(COUNT // 2,))
t2 = Thread(target=countdown, args=(COUNT // 2,))
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
print(time.time() - start)

p.terminate()
