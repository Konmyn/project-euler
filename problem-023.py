#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_abundant_number(number):
    divisor = 2
    divisors = set([1])
    while divisor <= number**0.5:
        if not number % divisor:
            divisors.add(divisor)
            divisors.add(number / divisor)
        divisor += 1
    if sum(divisors) > number:
        return True
    else:
        return False

def main():
    uplimit = 28123
    number = 13
    abundant_number_list = [12]
    while number <= uplimit:
        if is_abundant_number(number):
            abundant_number_list.append(number)
        number += 1
    total_sum = sum(range(24))
    natural = 25
    while natural <= uplimit:
        for anum in abundant_number_list:
            is_target = True
            if (natural - anum) in abundant_number_list:
                is_target = False
                break
            if anum*2 > natural:
                break
        if is_target:
            total_sum += natural
        natural += 1
    print total_sum


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
