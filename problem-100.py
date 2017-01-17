#!/usr/bin/python
# -*- coding: utf-8 -*-

# when number is too long, this function fails.
def is_perfect_square(number):
    long(number)
    return int(number**0.5)**2 == number

def main():
    number = 10**12 + 1
    while True:
        target = (number*(number - 1)*2 + 1)
        if is_perfect_square(target):
            print target
        number += 1

if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
