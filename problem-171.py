#!/usr/bin/python
# -*- coding: utf-8 -*-


def sum_of_squares_of_digits(number):
    the_sum = 0
    while number:
        the_sum += (number%10)**2
        number //=10
    return the_sum

def is_perfect_square(number):
    return int(number**0.5)**2 == number

def main():
    limit = 1000
    number = 1
    while number <= limit:
        sd = sum_of_squares_of_digits(number)
        if is_perfect_square(sd):
            print number, sd
        number += 1

if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
