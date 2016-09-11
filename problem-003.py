#!/usr/bin/python
# -*- coding: utf-8 -*-

target = 600851475143
stop = target
factors_list = []
number_try = 3
while number_try <= stop:
    if target%number_try == 0:
        factors_list.append(number_try)
        target /= number_try
        number_try -= 2
    number_try += 2
    stop = int(target**(0.5)+1)
print factors_list
print sum(factors_list)
