#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time-start_time)

def main():
    fib_stop = 4000000
    a = 1
    b = 2
    c = a+b
    target_list = [2]
    while c<=fib_stop:
        c = a+b
        if c%2 == 0:
            target_list.append(c)
        a = b
        b = c
    print "Result: {}".format(sum(target_list))