#!/usr/bin/python
# -*- coding: utf-8 -*-

SQUARE_DICT = {}
LOOP_DICT = {}

def generate_square_dict():
    global SQUARE_DICT
    for i in xrange(10):
        SQUARE_DICT[i]=i*i
    return SQUARE_DICT

def digit_square_sum(n):
    global SQUARE_DICT
    sq_sum = 0
    while n:
        sq_sum += SQUARE_DICT[n%10]
        n /= 10
    return sq_sum

def generate_loop_dict():
    # 9**2*7(digits)=567
    global LOOP_DICT
    generate_square_dict()
    for i in xrange(1, 568):
        n = i
        while True:
            if n == 89:
                LOOP_DICT[i] = 89
                break
            elif n == 1:
                LOOP_DICT[i] = 1
                break
            else:
                n = digit_square_sum(n)

def main():
    global LOOP_DICT
    generate_loop_dict()
    counter_89 = 0
    for v in LOOP_DICT.itervalues():
        if v == 89:
            counter_89 += 1
    for n in xrange(568, 10**7):
        if LOOP_DICT[digit_square_sum(n)] == 89:
            counter_89 += 1
    print "Result: {}".format(counter_89)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
