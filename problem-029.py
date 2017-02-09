#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


@runTime
def bruteForce(B=2, E=100):
    l = xrange(B, E+1)
    print "Result: {}".format(len({a**b for a in l for b in l}))

@runTime
def generalBruteForce(aB=2, aE=100, bB=2, bE=100):
    print "Result: {}".format(len({a**b for a in xrange(aB, aE+1) for b in xrange(bB, bE+1)}))


if __name__ == "__main__":
    bruteForce()
    generalBruteForce()
