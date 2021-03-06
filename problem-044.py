#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


@runTime
def bruteForce():
    # set() is a key data structure, use list would cause 100+ times time cost.
    pent_set = set()
    i = 0
    while True:
        i += 1
        pent = (3*i*i - i)/2
        for p in pent_set:
            if pent-p in pent_set and pent-2*p in pent_set:
                print "Result: {}".format(pent-2*p)
                return
        pent_set.add(pent)


if __name__ == "__main__":
    bruteForce()
