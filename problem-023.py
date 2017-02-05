#!/usr/bin/python
# -*- coding: utf-8 -*-


def proper_divisors_sum(natural):
    if natural == 1:
        return 0
    divisors = set([1])
    n = 2
    while n*n<=natural:
        if natural%n==0:
            divisors.update([n, natural/n])
        n += 1
    return sum(divisors)

def main():
    uplimit = 20162 # 28123
    total_sum = 0
    # set() reduce time cost from 400+s by list method to 1+s
    abundant_number_set = set()
    for n in xrange(1, uplimit):
        if proper_divisors_sum(n) > n:
            abundant_number_set.add(n)
        if any((n-i in abundant_number_set) for i in abundant_number_set):
            continue
        # n max is 20161
        total_sum += n
    print total_sum


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
