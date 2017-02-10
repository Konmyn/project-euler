#!/usr/bin/python
# -*- coding: utf-8 -*-


from fractions import gcd
from tools.runningTime import runTime


@runTime
def bruteForce():
    n_t = []
    for nomi in xrange(11, 99):
        denomi = nomi%10*10+nomi//10
        while denomi%10 and denomi>nomi:
            if denomi%10*nomi == nomi//10*denomi:
                n_t.append((nomi, denomi, nomi//10, denomi%10))
            denomi += 1
    no_pro = reduce(lambda x, y: x*y, [i[2] for i in n_t], 1)
    de_pro = reduce(lambda x, y: x*y, [i[3] for i in n_t], 1)
    g = gcd(no_pro, de_pro)
    print "Result: {}".format(de_pro//g)

@runTime
def reverseBruteForce():
    d = 1
    for i in xrange(1, 10):
        for j in xrange(1, i):
            q, r = divmod(9*j*i, 10*j-i)
            if not r and q <=9:
                d *= i/float(j)
    print "Result: {}".format(int(d))


if __name__ == "__main__":
    bruteForce()
    reverseBruteForce()
