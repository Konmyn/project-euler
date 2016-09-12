#!/usr/bin/python
# -*- coding: utf-8 -*-

def is_prime(number):
    if number == 2:
        return True
    if number%2 == 0:
        return False
    factor = 3
    stop_num = int(number**(0.5)+1)
    while factor <= stop_num:
        if number%factor == 0:
            return False
        factor += 2
    return True

def main():
    while True:
        in_number = input("Input the number you want to evaluate:")
        if isinstance(in_number, int):
            if is_prime(in_number):
                print "The number you input is PRIME."
            else:
                print "NOT prime!"
            confirm = raw_input("Continue?(Y/n)").lower()
            if confirm in ['yes', 'y']:
                continue
            else:
                break
        else:
            print "BAD input!"
            continue
        print "~~~~~BYE BYE!~~~~~"

if __name__ == "__main__":
    main()