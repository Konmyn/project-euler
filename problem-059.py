#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    print "Result: {}".format()


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
