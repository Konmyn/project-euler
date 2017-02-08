#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


def fn(number):
    stop = int(pow(number, 0.5))
    # always including 1 and the number itself
    # but if number=1, return 1
    count = 1
    for i in xrange(2, stop+1):
        if number%i == 0:
            count += 1
    return count*2 - (1 if stop**2 == number else 0)

@runTime
def brute_force_method(limit=500):
    s , natural= 1, 1
    while fn(s) <= limit:
        natural += 1
        s += natural
    print "Result: {}".format(s)

cache = {}
# memory version of above fn().
def factors(number):
    global cache
    if number in cache:
        return cache[number]
    stop = int(pow(number, 0.5))
    # always including 1 and the number itself
    # but if number=1, return 1
    count = 1
    for i in xrange(2, stop+1):
        if number%i == 0:
            count += 1
    result = count*2 - (1 if stop**2 == number else 0)
    cache[number] = result
    return result

@runTime
def light_use_formula(limit=500):
    fn, n = 0, 0
    while fn<limit:
        tri = n*(n+1)/2
        fn = factors((n+1)/2)*factors(n) if n%2 else\
                 factors(n/2)*factors(n+1)
        n += 1
    print "Result: {}".format(tri)


if __name__ == "__main__":
    brute_force_method()
    light_use_formula()
