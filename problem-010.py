#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import prime_sieve


# this method is source from problem 88, seems to be a bit slow.
def prime_list(upper_limit):
    primes = [2]
    if not isinstance(upper_limit, int):
        return []
    if upper_limit < 2:
        return []
    n = 3
    _is_prime = True
    while n < upper_limit:
        for i in primes:
            if not n % i:
                _is_prime = False
                break
        if _is_prime:
            primes.append(n)
        n += 2
        # if n % 10000 == 1:
        #     print n
        _is_prime = True
    return primes

# 80 (644s to 8.5s)times faster than function above in my A53SV.
def sum_prime(upper_limit):
    sum_pr = 2
    if upper_limit < 2:
        return 0
    if upper_limit == 2:
        return sum_pr
    number = 3
    while number < upper_limit:
        stop_num = int(pow(number, 0.5))
        factor = 3
        _is_prime = True
        while factor <= stop_num:
            if not number % factor:
                _is_prime = False
                break
            factor += 2
        if _is_prime:
            sum_pr += number
        number += 2
    return sum_pr

@runTime
def brute_force_method(upper_limit=2*10**6):
    sum_pr = sum_prime(upper_limit)
    print "Result: {}".format(sum_pr)

@runTime
def by_prime_sieve(upper_limit=2*10**6):
    print "Result: {}".format(sum(prime_sieve(upper_limit)))

if __name__ == "__main__":
    brute_force_method()
    by_prime_sieve()
