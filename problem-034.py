#!/usr/bin/python
# -*- coding: utf-8 -*-

# 0! is one!!!!!
FACTORIAL_DICT = {0: 1,}

def generate_factorial_dict():
    for natural in range(1, 10):
        FACTORIAL_DICT[natural] = reduce(lambda x,y: x*y, range(1, natural+1))

def digits_fac_sum(natural):
    the_sum = 0
    while natural:
        the_sum += FACTORIAL_DICT[natural%10]
        natural //= 10
    return the_sum

def main():
    generate_factorial_dict()
    # 9!*7 = 2540160
    uplimit = 2540160
    natural = 3
    datas = []
    while natural < uplimit:
        if natural == digits_fac_sum(natural):
            datas.append(natural)
        natural += 1
    print "Result: {}".format(sum(datas))


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
