#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    i, j = 1, 1
    n = 1
    while True:
        i, j = j, i+j
        n += 1
        if i > 10**(1000-1):
            break
    print "Result: {}".format(n)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
