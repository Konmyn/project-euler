#!/usr/bin/python
# -*- coding: utf-8 -*-


def digits_fifth_power(number):
    di_sum = 0
    while number:
        di_sum += (number%10)**5
        number //= 10
    return di_sum

def main():
    # 9**5*6 = 354294
    uplimit = 354294
    natural = 2
    target = []
    while natural<uplimit:
        if digits_fifth_power(natural) == natural:
            target.append(natural)
        natural += 1
    print target
    print "Result: {}".format(sum(target))


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
