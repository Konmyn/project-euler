#!/usr/bin/python
# -*- coding: utf-8 -*-


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
    print 'Program to testify your input number whether or not a prime.\n\
Hit Ctrl+C to stop this program.'
    while True:
        in_number = input("Input the number you want to evaluate:")
        if isinstance(in_number, int):
            if is_prime(in_number):
                print "The number you input is PRIME."
            else:
                print "NOT prime!"
        else:
            print "BAD input!"
            continue


if __name__ == "__main__":
    main()
