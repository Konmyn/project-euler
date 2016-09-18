#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    stop_p = 1000
    p = 3
    count = 0
    result = {'p': p, 'count': count}
    while p <= stop_p:
        count = right_angle_triangle_count(p)
        if count > result['count']:
            result['count'] = count
            result['p'] = p
        p += 1
    print "Within {}(include), p={} have the maximum solutions, which is {}.".format(stop_p, result['p'], result['count'])


def right_angle_triangle_count(primeter):
    count = 0
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
                count += 1
            a += 1
        c -= 1
        a = 1
        sum_ab = primeter - c
    return count


def is_right_angle_triangle(low, medium, high):
    if pow(low, 2) + pow(medium, 2) == pow(high, 2):
        return True
    return False


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
