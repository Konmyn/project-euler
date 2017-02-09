#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import DigitsPowerSum as DPS


# the key is to find the edge of this list.
@runTime
def bruteForce(exp=5):
    # one obvious up-edge is 9**5*6 = 354294
    # one edge is 9**exp*(exp-1) which is more efficient.
    print "Result: {}".format(sum([n for n in xrange(11, 9**exp*(exp-1)) if DPS(n, exp)==n]))


if __name__ == "__main__":
    bruteForce()
