#!/usr/bin/python
# -*- coding: utf-8 -*-


def expansions(n):
    numerator, denumerator = 1, 2
    while n != 1:
        numerator, denumerator = denumerator, denumerator*2+numerator
        n -= 1
    numerator, denumerator = numerator+denumerator, denumerator
    return (numerator, denumerator)

def main():
    n = 1
    counter = 0
    while n <= 1000:
        j, k = expansions(n)
        if len(str(j))>len(str(k)):
            counter += 1
        n += 1
    print "Result: {}".format(counter)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
