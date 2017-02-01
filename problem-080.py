#!/usr/bin/python
# -*- coding: utf-8 -*-


from decimal import *


# decimal digits means start from the beginning, not from '.'
def main():
    getcontext().prec=105
    natural = 1
    exclude_list = [i**2 for i in range(1, 11)]
    digits_sum = 0
    while natural <= 100:
        if natural not in exclude_list:
            n = Decimal(natural).sqrt()
            digits = ''.join(str(n).split('.'))[:100]
            for digit in digits:
                digits_sum += int(digit)
        natural += 1
    print "Result: {}".format(digits_sum)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
