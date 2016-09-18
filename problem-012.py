#!/usr/bin/python
# -*- coding: utf-8 -*-


def factors(number):
    stop = int(pow(number, 0.5))
    # always including 1 and the number itself
    count = 2
    i = 2
    while i <= stop:
        if not number % i:
            count += 2
        i += 1
    if pow(i-1, 2) == number:
        count -= 1
    return count


def main():
    triangle_number = 0
    number = 0
    while True:
        number += 1
        triangle_number += number
        if factors(triangle_number) > 500:
            break
    print "Result: {}".format(triangle_number)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
