#!/usr/bin/python
# -*- coding: utf-8 -*-


import itertools


my_list = range(1, 7)
target = 10

comb = itertools.combinations(my_list, 3)

re_list = [i for i in comb if sum(i)==target]
print(re_list)
