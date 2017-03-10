#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


@runTime
def bruteForce():
    for i in xrange(1000000):
        for j in [0, 1, 2, 3, 4]:
            for k in [3, 7]:
                n = (j*10**7+i*10+k)+10**8
                ns = str(n**2)
                if ns[::2] == "123456789":
                    print "Result: {}".format(n*10)
                    return


if __name__ == "__main__":
    bruteForce()
