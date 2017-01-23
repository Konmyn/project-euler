#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    result = 0
    number = 1
    while number<=1000:
        result += pow(number, number)%10**10
        result %= 10**10
        number += 1
    print "Result: {}".format(result)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
