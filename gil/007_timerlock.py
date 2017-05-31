#!/usr/bin/python
# -*- coding: utf-8 -*-


import time
import threading


tLock = threading.Lock()


def timer(name, delay, repeat):
    print('Timer {} started'.format(name))
    tLock.acquire()
    print('{} has acquired the lock'.format(name))
    while repeat>0:
        time.sleep(delay)
        print('{}: {}'.format(name, time.ctime(time.time())))
        repeat -= 1
    print('{} is releasing the lock'.format(name))
    tLock.release()
    print('Timer {} completed'.format(name))


def main():
    t1 = threading.Thread(target=timer, args=('Timer1', 1, 5))
    t2 = threading.Thread(target=timer, args=('Timer2', 2, 5))
    t1.start()
    t2.start()
    print('main completed')

if __name__ == '__main__':
    main()
