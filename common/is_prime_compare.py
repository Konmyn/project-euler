#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_prime_1(n):
    """Returns True if n is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if not n % 2:
        return False

    factor = 3
    stop_n = int(pow(n, 0.5))

    while factor <= stop_n:
        if not n % factor:
            return False

        factor += 2

    return True


def is_prime_2(n):
    """Returns True if n is prime."""
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


def miller_rabin(n, k=40):
    import random

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in xrange(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in xrange(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def main():
    # Mersenne Primes
    # n = pow(2, 61) - 1 ->90s/60s
    n = pow(2, 31) - 1

    from timeit import default_timer

    start_time = default_timer()
    result = is_prime_1(n)
    end_time = default_timer()
    print "Result: {}".format(result)
    print "Time used(s): {}".format(end_time - start_time)

    start_time = default_timer()
    result = is_prime_2(n)
    end_time = default_timer()
    print "Result: {}".format(result)
    print "Time used(s): {}".format(end_time - start_time)

    start_time = default_timer()
    result = miller_rabin(n)
    end_time = default_timer()
    print "Result: {}".format(result)
    print "Time used(s): {}".format(end_time - start_time)


if __name__ == "__main__":
    main()
