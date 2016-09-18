#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_prime(number):
    if number == 2:
        return True
    if not number % 2:
        return False
    factor = 3
    stop_num = int(pow(number, 0.5))
    while factor <= stop_num:
        if not number % factor:
            return False
        factor += 2
    return True


def prime_list(upper_limit):
    n = 2
    list_primes = []
    while n <= upper_limit:
        if is_prime(n):
            list_primes.append(n)
        n += 1
    return list_primes


def main():
    limits = 1000
    primes = prime_list(limits)
    i = 1
    while sum(primes[:i]) < limits:
        i += 1
    i -= 1
    max_possible = i
    _loop = True
    while _loop:
        j = 0
        while j <= (max_possible - i):
            if sum(primes[j:j + i]) in primes:
                _loop = False
                break
            j += 1
        i -= 1
    i += 1
    print "Result: {}".format(sum(primes[j:j + i]))


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
