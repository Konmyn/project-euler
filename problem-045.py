#!/usr/bin/python
# -*- coding: utf-8 -*-


def gen_pen(number):
    return number*(3*number - 1)/2

def generate_pentagonal_number():
    natural = 1
    while True:
        yield (natural, gen_pen(natural))
        natural += 1

def is_pentagonal(start, to_match):
    n = start + 1
    m = to_match
    while gen_pen(n)<=m:
        if gen_pen(n) == m:
            return True
        n += 1
    return False

def main():
    pent_list = []
    flag = 0
    gen = generate_pentagonal_number()
    break_loop = False
    while True:
        cache = gen.next()
        pent_list.append(cache[1])
        flag = cache[0]
        loop, end = flag-2, flag-1
        while loop>0:
            if (pent_list[end]-pent_list[loop]) in pent_list[:loop]:
                print cache
                if is_pentagonal(end, pent_list[end]+pent_list[loop]):
                    D = pent_list[end]-pent_list[loop]
                    break_loop = True
                    break
            loop -= 1
        if break_loop:
            break
    print "Result: {}".format(D)

if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
