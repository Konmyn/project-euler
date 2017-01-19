#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_prime(n):
    if n < 2:
        return False
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

def is_truncatable_prime(number):
    from_right = number//10
    while from_right:
        if not is_prime(from_right):
            return False
        from_right //= 10
    num_len = len(str(number)) - 1
    from_left = number%(10**num_len)
    num_len -= 1
    while from_left:
        if not is_prime(from_left):
            return False
        from_left %= 10**num_len
        num_len -= 1
    return True

def main():
    number = 11
    counter = 0
    prime_list = []
    while counter < 11:
        if is_prime(number):
            if is_truncatable_prime(number):
                counter += 1
                prime_list.append(number)
        number += 1
    print prime_list
    print "Result: {}".format(sum(prime_list))


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
