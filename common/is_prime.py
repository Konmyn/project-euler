#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_prime(number):
    if number < 2:
        return False
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
