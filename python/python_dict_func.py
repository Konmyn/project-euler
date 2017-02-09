#!/usr/bin/python
# -*- coding: utf-8 -*-


# the dict that cache pointing to is not a local variable,
# it is somehow a golbal variable even it has no name.
def f(i, cache={1:1}):
    if i not in cache:
        cache[i] = f(i-1) + 1
        print cache
    return cache[i]

