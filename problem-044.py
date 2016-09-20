#!/usr/bin/python
# -*- coding: utf-8 -*-


def pentagonal_list(upper_limit):
    return [x * (3 * x - 1) / 2 for x in xrange(1, upper_limit + 1)]


def is_perfect_square(n):
    return pow(int(pow(n, 0.5)), 2) == n


def is_pentagonal_number(n):
    return is_perfect_square(24 * n + 1) and int(pow(24 * n + 1, 0.5)) % 6 == 5

def main():
    result = 0
    n = 1
    penta_list = list()
    while not result:
        penta_next = n * (3 * n - 1) / 2
        for penta in penta_list:
            if is_pentagonal_number(penta + penta_next):
                if is_pentagonal_number(penta + penta_next * 2):
                    result = penta
                    break
                elif is_pentagonal_number(penta * 2 + penta_next):
                    result = penta_next
                    break
        else:
            penta_list.append(penta_next)
            n += 1
    print "Result: {}".format(result)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
