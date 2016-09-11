#!/usr/bin/python
# -*- coding: utf-8 -*-

fib_stop=4000000
a = 1
b = 2
c = a+b
target_list = [2]
while c<=fib_stop:
    c = a+b
    if c%2==0:
        target_list.append(c)
    a = b
    b = c
print sum(target_list)
