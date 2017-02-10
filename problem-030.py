#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import DigitsPowerSum as DPS


# below function will give you a hint for the uplimit of this problem
@runTime
def numberStep(limit=9**5*6):
    step = [1, 1]
    for i in xrange(2, limit):
        s = DPS(i, 5)
        if s > step[-1]:
            step.extend([i, s])
    print step

# below function will print numbers that its DPS bigger than 9999 and in [10000, 89999).
# output: [19999, 29999, 39999, 49999, 59999, 69999, 79999, 88999, 89899, 89989, 89998]
@runTime
def oneMoreDigit():
    target = []
    st = DPS(9999, 5)
    for i in range(10000, 89999):
        if DPS(i, 5)> st:
            target.append(i)
    print target

# the key is to find the bounds of this list.
@runTime
def bruteForce(exp=5):
    # one obvious up-edge is 9**5*6 = 354294
    # one edge is 9**exp*(exp-1) which is more efficient. 9**5*4 = 236196
    print "Result: {}".format(sum([n for n in xrange(11, 9**exp*(exp-1)) if DPS(n, exp)==n]))


if __name__ == "__main__":
    # numberStep()
    # oneMoreDigit()
    bruteForce()
