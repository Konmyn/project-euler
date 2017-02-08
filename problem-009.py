#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime

# only fit for one or none result, can not deal with 2 or more possibilities.
def right_angle_triangle(primeter):
    # a<=b<=c, a+b+c=primeter
    for a in xrange(1, primeter/3+1):
        for b in xrange(a, (primeter-a)/2+1):
            c = primeter-a-b
            if a**2 + b**2 == c**2:
                return [a, b, c]
    return None

@runTime
def brute_force_method(length=1000):
    abc = right_angle_triangle(length)
    if abc:
        abc.append(reduce(lambda x, y: x * y, abc, 1))
        print "Result: {} * {} * {} = {}".format(*abc)
    else:
        print "Result: None"

def divisors(n):
    for i in xrange(1, int(n**0.5)+1):
        if n%i == 0:
            yield i, n/i

# a, b, c actually is Pythagorean triplet.
# https://en.wikipedia.org/wiki/Pythagorean_theorem
# below function use Dickson’s method
# https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples
@runTime
def by_formula(length=1000):
    pn = {}
    for r in range(int(length**0.5)/2*2, length/5, 2):
        st = r*r / 2
        for s, t in divisors(st):
            x = (r+s) + (r+t) + (r+s+t)
            pn[x] = (r+s) * (r+t) * (r+s+t)
    print "Result:", pn[length] if length in pn else "None"


if __name__ == "__main__":
    brute_force_method()
    by_formula()
