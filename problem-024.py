#!/usr/bin/python
# -*- coding: utf-8 -*-


from itertools import permutations


def main():
    perm = permutations(range(10))
    for i in xrange(1000000-1):
        perm.next()
    cache = perm.next()
    result = ''
    for i in cache:
        result += str(i)
    print "Result: {}".format(result)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
