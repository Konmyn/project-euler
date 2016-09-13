#!/usr/bin/python
# -*- coding: utf-8 -*-

def prime_list(upper_limit):
    primes = [2]
    if not isinstance(upper_limit, int):
        return []
    if upper_limit<2:
        return []
    n = 3
    _is_prime = True
    while n<=upper_limit:
        for i in primes:
            if n%i==0:
                _is_prime = False
                break
        if _is_prime:
            primes.append(n)
        n += 2
        _is_prime = True
    return primes

def factor_list(number, primes):
    i = 0
    prime_factors = []
    while primes[i]<=number:
        if number%primes[i]==0:
            prime_factors.append(primes[i])
            number /= primes[i]
            continue
        i += 1
    return prime_factors

def main():
    k = 323434
    upper_limit = k
    primes = prime_list(upper_limit)
    factors = factor_list(k, primes)
    print "Result: {}".format(factors)

if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time-start_time)