#!/usr/bin/python
# -*- coding: utf-8 -*-


def euler_totient_function_phi(n):
    result = n
    i = 2
    lock = n
    while i*i <= lock:
        if n%i == 0:
            result = result/i*(i-1)
            while n%i == 0:
                n //= i
        i += 1
    if n != 1:
        result = result/n*(n-1)
    return result

def main():
    n = 1
    max_cache = 0
    target = 0
    while n <= 1000000:
        cache = float(n)/euler_totient_function_phi(n)
        if cache > max_cache:
            result = n
            max_cache = cache
        n += 1
    print "Result: {}".format(result)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
