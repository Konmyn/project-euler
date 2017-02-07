#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


@runTime
def brute_force_method(L = 13):
    digits = map(int, ''.join(l.rstrip() for l in open("p008_number.txt")))
    if L>len(digits):
        print "Result: None"
        return
    else:
        # pay attention to boundary conditions.
        # digits[0:L] -> digits[len(digits)-L:len(digits)]
        target = max(reduce(lambda x, y: x*y, digits[i:i+L])\
                 for i in xrange(len(digits)-L+1))
    print "Result: {}".format(target)


if __name__ == "__main__":
    brute_force_method()
