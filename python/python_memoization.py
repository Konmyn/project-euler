#!/usr/bin/python
# -*- coding: utf-8 -*-


import time


ef_cache = dict()


def expensive_func(num):
    if num in ef_cache:
        return ef_cache[num]

    print("Computing {}...".format(num))
    time.sleep(1)
    result = num * num
    ef_cache[num] = result
    return result

if __name__ == "__main__":
    start = time.time()
    print(expensive_func(22))
    print(expensive_func(87))
    print(expensive_func(22))
    print(expensive_func(87))
    print("Time used: {} seconds".format(time.time() - start))
