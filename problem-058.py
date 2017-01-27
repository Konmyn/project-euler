#!/usr/bin/python
# -*- coding: utf-8 -*-

def is_prime(n):
    """Returns True if n is prime."""
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
    side_length = 1
    diagonal = 1
    walk = 1
    step = 2
    prime_count = 0
    while True:
        loop = 4
        while loop:
            walk += step
            if loop > 1 and is_prime(walk):
                prime_count += 1
            loop -= 1
        step += 2
        diagonal += 4
        side_length += 2
        if prime_count*10<diagonal:
            break
    print "Result: {}".format(side_length)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
