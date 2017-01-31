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

def init_prime_list(limit = 10**7):
    n = 2
    uplimit = int(pow(limit, 0.5))+1
    while n < uplimit:
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
    if len(str(result)) != len(str(lock)):
        return False
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

def is_permutation(n, m):
    n_list = []
    m_list = []
    while n:
        n_list.append(n%10)
        n //= 10
    while m:
        m_list.append(m%10)
        m //= 10
    n_list.sort()
    m_list.sort()
    return m_list == n_list

def main():
    limit = 10**7
    n = 2
    min_cache = 999999999999
    target = 0
    init_prime_list(limit)
    while n < limit:
        phi = phi_function(n)
        if phi and is_permutation(n, phi):
            cache = float(n)/phi
            if cache<min_cache:
                min_cache = cache
                target = n
                print target, min_cache
        n += 1
    print "Result: {}".format(target)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
