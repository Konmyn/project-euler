#!/usr/bin/python
# -*- coding: utf-8 -*-

PRIME_LIST = []

def is_prime(n):
    """Returns True if n is prime."""
    if n < 2:
        return False
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

def init_prime_list():
    n = 2
    while n < 1000:
        if is_prime(n):
            PRIME_LIST.append(n)
        n += 1
    return True

def phi_function(n):
    result = lock = n
    for i in PRIME_LIST:
        if n%i == 0:
            result = result/i*(i-1)
            while n%i == 0:
                n //= i
        if i*i > lock:
            break
    if n != 1:
        result = result/n*(n-1)
    return result

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
    init_prime_list()
    while n <= 1000000:
        # cache = float(n)/euler_totient_function_phi(n)
        cache = float(n)/phi_function(n)
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
