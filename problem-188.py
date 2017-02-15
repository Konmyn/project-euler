#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


# a↑↑1 = a**1
#a↑↑(k+1) = a**(a↑↑k)
def tetration(a, k):
    if k == 1:
        return a
    else:
        return a**tetration(a, k-1)

# RuntimeError: maximum recursion depth exceeded
@runTime
def bruteForce():
    T = tetration(1777, 1855)%10**8
    print "Result: {}".format(T)

# too big to store!
def hyperexponentiation(a, k):
    cache = 1
    while k>0:
        cache = a**cache
        k -= 1
    return cache

@runTime
def newBruteForce():
    T = hyperexponentiation(1777, 1855)%10**8
    print "Result: {}".format(T)

# Modulo operation
# https://en.wikipedia.org/wiki/Modulo_operation
# Modular arithmetic
# https://en.wikipedia.org/wiki/Modular_arithmetic
@runTime
def byInternalFunction(a=1777, k=1855, d=10**8):
    t0 = 1
    for i in xrange(k):
        t1 = pow(a, t0, d)
        if t0 == t1:
            break
        t0 = t1
    print "Result: {}".format(t1)


if __name__ == "__main__":
    # bruteForce()
    # newBruteForce()
    byInternalFunction()
