#!/usr/bin/python
# -*- coding: utf-8 -*-


def highest_common_factor(number_a, number_b):
    h_factor, factor = 1, 1
    stop = min(number_a, number_b)
    while factor <= stop:
        factor += 1
        if number_a % factor == 0 and number_b % factor == 0:
            h_factor = factor
    return h_factor

def hcf_is_one(number_a, number_b):
    if not number_a % 2 and not number_b % 2:
        return False
    stop = min(number_a, number_b)
    factor = 1
    while factor <= stop:
        factor += 2
        if not number_a % factor and not number_b % factor:
            return False
    return True


def main():
    n = 2
    stop = 20
    count_primes = prime_count(stop)
    primes = count_primes.keys()
    while n <= 20:
        for prime in primes:
            number = 0
            if not n % prime:
                _temp = n
                while not _temp % prime:
                    _temp /= prime
                    number += 1
                if count_primes[prime] < number:
                    count_primes[prime] = number
        n += 1
    result = 1
    print count_primes
    for k, v in count_primes.items():
        if v:
            result *= k**v
    print "Result: {}".format(result)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
