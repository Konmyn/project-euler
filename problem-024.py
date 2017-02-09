#!/usr/bin/python
# -*- coding: utf-8 -*-


from itertools import permutations
from tools.runningTime import runTime
from tools.common import permutation as perm


# stupid maybe
@runTime
def by_python_package(steps=10**6):
    perm = permutations(range(10))
    for i in xrange(steps-1):
        perm.next()
    print "Result: {}".format(''.join(map(str, perm.next())))

@runTime
def quick_perm(steps=10**6):
    print "Result: {}".format(perm(steps-1, "0123456789"))


if __name__ == "__main__":
    by_python_package()
    quick_perm()
