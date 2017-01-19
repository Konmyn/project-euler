#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    natural = 1
    product = 1
    length = 0
    for i in range(7):
        while True:
            length += len(str(natural))
            if length >= 10**i:
                product *= int(str(natural)[((len(str(natural))-(length-10**i))-1)])
                natural += 1
                break
            natural += 1
    print "Result: {}".format(product)

if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
