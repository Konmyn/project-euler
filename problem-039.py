#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


def right_angle_triangle_count(primeter):
    count = 0
    # a<=b<=c, a+b+c=primeter
    for c in xrange(primeter/2, int(primeter/2.4142), -1):
        for a in xrange(2, (primeter-c)/2+1):
            b = primeter-c-a
            if is_right_angle_triangle(a, b, c):
                count += 1
    return count

def is_right_angle_triangle(low, medium, high):
    if pow(low, 2) + pow(medium, 2) == pow(high, 2):
        return True
    return False

@runTime
def bruteForce(L=1000):
    result = {'p': 0, 'count': 0}
    for p in xrange(4, L+1, 2):
        count = right_angle_triangle_count(p)
        if count > result['count']:
            result['count'] = count
            result['p'] = p
    print "Within {}(include), p={} have the maximum solutions, which is {}.".format(L, result['p'], result['count'])

@runTime
def smartBruteForce(L=1000):
    t_max, p_max = 0, 0
    for p in range(L//4*2, L+1, 2):
        t = 0
        # why not a start from 1?
        # just think about a**2 + b**2 = c**2
        for a in range(2, int(p/3.4142)+1):
            if p*(p-2*a)%(2*(p-a)) == 0:
                t += 1
                if t>t_max:
                    t_max = t
                    p_max = p
    print "Within {}(include), p={} have the maximum solutions, which is {}.".format(L, p_max, t_max)


if __name__ == "__main__":
    bruteForce()
    smartBruteForce()
