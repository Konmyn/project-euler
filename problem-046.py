#!/usr/bin/python
# -*- coding: utf-8 -*-


PRIME_LIST = [2,3,5,7]

def is_the_sum(n_odd):
    n = 1
    while n**2*2<n_odd:
        if is_prime(n_odd-n**2*2):
            return True
        n += 1
    return False

def is_in_prime(number):
    if number in PRIME_LIST:
        return True
    else:
        return False

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
    odd = 7
    while True:
        odd += 2
        if is_prime(odd):
            PRIME_LIST.append(odd)
            continue
        if not is_the_sum(odd):
            break
    print PRIME_LIST
    print "Result: {}".format(odd)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
