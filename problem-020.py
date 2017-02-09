#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import factorial as f

# Python has inherent large precision integers.
@runTime
def on_my_own(natural=100):
    product, the_sum = f(natural), 0
    while product:
        the_sum, product = the_sum+product%10, product/10
    print "Result: {}".format(the_sum)

@runTime
def one_line(natural=100):
    print "Result: {}".format(sum(map(int, str(f(natural)))))

if __name__ == "__main__":
    on_my_own()
    one_line()
