#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


@runTime
def on_my_own(number=2**1000):
    digits_sum = 0
    while number:
        digits_sum, number = digits_sum + number % 10, number/10
    print "Result: {}".format(digits_sum)

@runTime
def short_expression(n=2**1000):
    print "Result: {}".format(sum(map(int, str(n))))

if __name__ == "__main__":
    on_my_own()
    short_expression()
