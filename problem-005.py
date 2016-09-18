#!/usr/bin/python
# -*- coding: utf-8 -*-


def prime_count(upper_limit):
    _values = 0
    primes = {2: _values}
    if not isinstance(upper_limit, int):
        return {}
    if upper_limit < 2:
        return {}
    n = 3
    _is_prime = True
    while n <= upper_limit:
        for k in primes.iterkeys():
            if not n % k:
                _is_prime = False
                break
        if _is_prime:
            primes[n] = _values
        n += 2
        _is_prime = True
    return primes


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
