#!/usr/bin/python
# -*- coding: utf-8 -*-


PRIME_LIST = []

def prime_factor_number(number):
    if is_prime(number):
        PRIME_LIST.append(number)
        return 1
    counter = 0
    for p in PRIME_LIST:
        if number%p == 0:
            counter += 1
            number //= p
        if number<p:
            break
    return counter

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

def main():
    number = 1
    while True:
        number += 1
        if prime_factor_number(number) >= 4:
            number += 1
            if prime_factor_number(number) >= 4:
                number += 1
                if prime_factor_number(number) >= 4:
                    number += 1
                    if prime_factor_number(number) >= 4:
                        break
    print PRIME_LIST
    print "Result: {}".format(number-3)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
