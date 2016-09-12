#!/usr/bin/python
# -*- coding: utf-8 -*-

def is_prime(number):
    if number == 2:
        return True
    if number%2 == 0:
        return False
    factor = 3
    stop_num = int(number**(0.5)+1)
    while factor <= stop_num:
        if number%factor == 0:
            return False
        factor += 2
    return True

target = 600851475143
stop = int(target**(0.5)+1)
number_try = 3
while number_try <= stop:
    if target%number_try == 0:
        candidate = target/number_try
        if is_prime(candidate):
            print "Result:", candidate
            break
    number_try += 2
print "Operation round:", (number_try-1)/2