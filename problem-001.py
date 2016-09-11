#!/usr/bin/python
# -*- coding: utf-8 -*-

n = 0
target_list = []
while n<1000:
    if n%3 == 0:
        target_list.append(n)
    elif n%5 == 0:
        target_list.append(n)
    n += 1
print target_list
print sum(target_list)
