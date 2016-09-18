#!/usr/bin/python
# -*- coding: utf-8 -*-


def primes_dict(counts):
    _key = 1
    primes = {_key: 2}
    if not isinstance(counts, int):
        return {}
    if counts < 1:
        return {}
    if counts == 1:
        return primes
    n = 3
    _key += 1
    _is_prime = True
    while _key <= counts:
        for v in primes.itervalues():
            if not n % v:
                _is_prime = False
                break
        if _is_prime:
            primes[_key] = n
            _key += 1
        n += 2
        _is_prime = True
    return primes


def main():
    counts = 10001
    the_prime = primes_dict(counts)
    print "Result: {}".format(the_prime[counts])


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
