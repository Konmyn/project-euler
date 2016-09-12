#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time-start_time)

def main():
    n = 1
    target_list = []
    while n<1000:
        if n%3 == 0:
            target_list.append(n)
        elif n%5 == 0:
            target_list.append(n)
        n += 1
    print "Result: {}".format(sum(target_list))