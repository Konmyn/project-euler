#!/usr/bin/python
# -*- coding: utf-8 -*-


from timeit import default_timer
from random import randint

list_length = 10000
rand_length = 10000

list_a = range(list_length)
set_b = set(list_a)
list_c = [randint(0, 2*rand_length-1) for i in xrange(rand_length)]

# caculate time cost in list lookup, should be O(n)
list_start_time = default_timer()
list_d = [1 if i in list_a else 0 for i in list_c]
count = sum(list_d)
print "Result: {}".format(count)
list_end_time = default_timer()
list_time = list_end_time - list_start_time
print "Time used(s) by list: {}".format(list_time)

# caculate time cost in set lookup, should be O(1)
set_start_time = default_timer()
list_e = [1 if i in set_b else 0 for i in list_c]
count = sum(list_e)
print "Result: {}".format(count)
set_end_time = default_timer()
set_time = set_end_time - set_start_time
print "Time used(s) by set: {}".format(set_time)

print "list:set = {} in a {}X{} search".format(list_time/set_time,
                                               list_length, rand_length)
