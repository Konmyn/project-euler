#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


@runTime
def on_my_own():
    number_list = map(int, open("p013_numbers.txt").readlines())
    number_sum = str(sum(number_list))[:10]
    print "Result: {}".format(number_sum)


if __name__ == "__main__":
    on_my_own()
