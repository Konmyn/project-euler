#!/usr/bin/python
# -*- coding: utf-8 -*-


def digital_sum(n):
    suma = 0
    while n:
        suma += n%10
        n //= 10
    return suma

def main():
    maxsum = 0
    a = 1
    while a<100:
        b = 1
        while b<100:
            maxsum = max(maxsum, digital_sum(a**b))
            b += 1
        a += 1
    print "Result: {}".format(maxsum)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
