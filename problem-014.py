#!/usr/bin/python
# -*- coding: utf-8 -*-


def chain_length(number):
    length = 1
    while number != 1:
        if number % 2:
            number = 3 * number + 1
            length += 1
        else:
            number /= 2
            length += 1
    return length


def main():
    number = 1
    max_length = 0
    while number < 1000000:
        length = chain_length(number)
        if length > max_length:
            max_length = length
            target = number
        number += 1
    print "Result: {} has longest chain {}".format(target, max_length)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
