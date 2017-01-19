#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    dis_set = set()
    a = 2
    while a<=100:
        b = 2
        while b<=100:
            dis_set.add(a**b)
            b += 1
        a += 1
    print "Result: {}".format(len(dis_set))


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
