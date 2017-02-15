#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


# 28433×2**7830457+1
@runTime
def bruteForce():
    cache = 1
    dl = 10**10
    for i in xrange(7830457):
        cache = (cache*2)%dl
    cache = (cache*28433+1)%dl
    print "Result: {}".format(cache)

@runTime
def newBruteForce():
    print "Result: {}".format((28433*2**7830457+1)%10**10)


if __name__ == "__main__":
    bruteForce()
    newBruteForce()
