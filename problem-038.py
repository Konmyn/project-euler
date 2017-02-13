#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import is_pandigital


target = []

def list_init():
    list_serial = []
    for i in range(3, 11):
        list_serial.append(range(1, i))
    return list_serial

def seek_edge(num_list):
    num_len = len(num_list)
    if num_len == 2:
        return (5000, 10000)
    if num_len == 3:
        return (100, 334)
    if num_len == 4:
        return (10, 100)
    if num_len >= 5:
        return (1, 99)

def pass_to_list(number, num_list):
    strings = ''
    for num in num_list:
        strings += str(num*number)
    if '0' in strings or len(strings) != 9:
        return
    if len(set(strings)) == 9:
        target.append(int(strings))

@runTime
def bruteForce():
    num_list = list_init()
    for nums in num_list:
        start, limit = seek_edge(nums[:])
        while start<limit:
            pass_to_list(start, nums[:])
            start += 1
    print target
    print "Result: {}".format(max(target))

# read the question.
# find out the bound and narrow it as possible.
# 需要花在思考上面的时间多于编程的时间。
@runTime
def smartBruteForce():
    for i in xrange(9487, 9123, -1):
        r = i*10**5+2*i
        if is_pandigital(r, 9):
            print "Result: {}".format(r)
            return
    print "None Found."


if __name__ == "__main__":
    bruteForce()
    smartBruteForce()
