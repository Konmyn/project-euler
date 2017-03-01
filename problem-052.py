#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


def contain_same_digits(n):
    counter = [0]*10
    cache = n
    while cache:
        counter[cache%10] += 1
        cache //= 10
    for i in range(2, 7):
        cache = n*i
        counteri = [0]*10
        while cache:
            counteri[cache%10] += 1
            cache //= 10
        if counter != counteri:
            return False
    return True

@runTime
def bruteForce():
    # start from 10
    power = 1
    while True:
        natural = pow(10, power)
        limit = 10*natural
        while natural*6<limit:
            if contain_same_digits(natural):
                print "Result: {}".format(natural)
                return
            natural += 1
        power += 1


@runTime
def byMagic():
    f = lambda n:sorted(str(n))
    n = 99999
    while not f(n*2) == f(n*3) == f(n*4) == f(n*5) ==f(n*6):
        n += 9
    print "Result: {}".format(n)


if __name__ == "__main__":
    bruteForce()
    byMagic()
