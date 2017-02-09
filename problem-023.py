#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import proper_divisors_sum as ps

# According to Wolfram Mathworld’s discussion on Abundant Numbers,
# “Every number greater than 20161 can be expressed as a sum of two abundant numbers.”
# So our upper bound is 20161 instead of 28123.
@runTime
def after_learned():
    uplimit, total_sum = 20162, 0 # 28123
    # set() reduce time cost from 400+s by list method to 1+s
    abn = set()
    for n in xrange(1, uplimit):
        if ps(n) > n:
            abn.add(n)
        # Numbers that are not the sum of two abundant numbers (not necessarily distinct).
        # https://oeis.org/A048242
        if any((n-i in abn) for i in abn):
            continue
        total_sum += n
    print "Result: {}".format(total_sum)


if __name__ == "__main__":
    after_learned()
