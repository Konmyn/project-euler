#!/usr/bin/python
# -*- coding: utf-8 -*-


PRIME_LIST = []

def gen_prime_list(start=1000, stop=9999):
    number = start
    while number<=stop:
        if is_prime(number):
            PRIME_LIST.append(number)
        number += 1
    return

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

def is_permutation(x, y, z):

def main():
    gen_prime_list()
    candidates = []
    i = len(PRIME_LIST)-1
    while i>1:
        j = i-1
        while j>0:
            if PRIME_LIST[i]-PRIME_LIST[j] in PRIME_LIST[:j]:
                if is_permutation(PRIME_LIST[i]-PRIME_LIST[j], PRIME_LIST[j], PRIME_LIST[i]):
                    candidates.extend([PRIME_LIST[i]-PRIME_LIST[j], PRIME_LIST[j], PRIME_LIST[i]])
            j -= 1
        i -= 1
    print "Result: {}".format(candidates)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
