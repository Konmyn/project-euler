#!/usr/bin/python
# -*- coding: utf-8 -*-

FACTORIAL_DICT = {0: 1,}

def init_factorial_dict(end = 9):
    for i in range(1, end+1):
        FACTORIAL_DICT[i] = FACTORIAL_DICT[i-1]*i

def digit_factorial(n):
    factorial = 0
    while n:
        factorial += FACTORIAL_DICT[n%10]
        n /= 10
    return factorial

def terms_equals_to_60(n):
    terms_list = [n]
    while len(terms_list) < 60:
        n = digit_factorial(n)
        if n not in terms_list:
            terms_list.append(n)
        else:
            return False
    return True

def main():
    init_factorial_dict()
    n = 1
    terms_counter = 0
    while n < 1000000:
        if terms_equals_to_60(n):
            terms_counter += 1
        n += 1
    print "Result: {}".format(terms_counter)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
