#!/usr/bin/python
# -*- coding: utf-8 -*-


from datetime import date as Date


def main():
    counter = 0
    day = 1
    for year in range(1901, 2001):
        for month in range(1, 13):
            if Date(year, month, day).weekday() == 6:
                counter += 1
    print "Result: {}".format(counter)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
