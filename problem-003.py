#!/usr/bin/python
# -*- coding: utf-8 -*-

def main(target):
    stop = int(target**(0.5)+1)
    number_try = 3
    while number_try <= stop:
        if not target%number_try:
            candidate = target/number_try
            if is_prime(candidate):
                print "Result: {}".format(candidate)
                break
            target = candidate
            continue
        number_try += 2
    print "Operation rounds: {}".format((number_try-1)/2)

def is_prime(number):
    if number == 2:
        return True
    if not number%2:
        return False
    factor = 3
    stop_num = int(pow(number, 0.5))
    while factor <= stop_num:
        if not number%factor:
            return False
        factor += 2
    return True

theNumber = 600851475143

if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main(theNumber)
    end_time = default_timer()
    print "Time used(s): {}".format(end_time-start_time)