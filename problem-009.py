#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


# source from problem 39
def is_right_angle_triangle(low, medium, high):
    if pow(low, 2) + pow(medium, 2) == pow(high, 2):
        return True
    return False


def right_angle_triangle_list(primeter):
    # a<=b<=c, a+b+c=primeter
    a = 1
    b = 1
    sum_ab = a + b
    c = primeter - sum_ab
    stop_point = primeter / 3
    while c > stop_point:
        while a <= sum_ab / 2:
            b = sum_ab - a
            if is_right_angle_triangle(a, b, c):
                count = [a, b, c]
                c = stop_point
                break
            a += 1
        c -= 1
        a = 1
        sum_ab = primeter - c
    return count

@runTime
def brute_force_method():
    sum_abc = 1000
    _abc = right_angle_triangle_list(sum_abc)
    product = reduce(lambda x, y: x * y, _abc, 1)
    print "Result: {} * {} * {} = {}".format(_abc[0], _abc[1], _abc[2], product)


if __name__ == "__main__":
    brute_force_method()
