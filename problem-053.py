#!/usr/bin/python
# -*- coding: utf-8 -*-


# 0! == 1
factorial = [1]

def init_factorial(limit=100):
    n = 1
    while n <= limit:
        factorial.append(n*factorial[n-1])
        n += 1

def combinations(n, r):
    return (factorial[n]/factorial[r])/factorial[n-r]

def main():
    init_factorial()
    print factorial
    n = 1
    counter = 0
    while n<=100:
        i = 1
        while i<=n:
            if combinations(n, i) > 10**6:
                counter += 1
            i += 1
        n += 1
    print "Result: {}".format(counter)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
