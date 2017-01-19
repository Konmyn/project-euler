#!/usr/bin/python
# -*- coding: utf-8 -*-


def quadratics_form(n, a, b):
    return (n**2 + a*n + b)

def is_prime(n):
    if n < 2:
        return False
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    # a prime (except 2 and 3) is of form 6k - 1 or 6k + 1
    while i * i <= n:
        if not n % i or not n % (i + 2):
            return False
        i += 6
    return True

def main():
    record = {'a':0, 'b':0, 'len':0}
    a = -999
    while a<1000:
        b = -1000
        while b<=1000:
            n = 0
            chain_len = 0
            while is_prime(quadratics_form(n, a, b)):
                n += 1
                chain_len += 1
            if chain_len > record['len']:
                record['a'] = a
                record['b'] = b
                record['len'] = chain_len
                print record
            b += 1
        a += 1
    print "Result: {}".format(record['a']*record['b'])


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
