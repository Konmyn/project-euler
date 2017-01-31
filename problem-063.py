#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    cache = 0
    candidates = []
    power = 1
    while True:
        cache = len(candidates)
        number = 1
        num_pow = pow(number, power)
        while len(str(num_pow)) <= power:
            if len(str(num_pow)) == power:
                candidates.append(num_pow)
            number += 1
            num_pow = pow(number, power)
        power += 1
        length = len(candidates)
        if cache == length:
            break
    print "Result: {}".format(length)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
