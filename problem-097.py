#!/usr/bin/python
# -*- coding: utf-8 -*-


# 28433×2**7830457+1
def main():
    cache = 1
    digit_save = 10**10
    for i in xrange(7830457):
        cache = (cache*2)%digit_save
    cache = (cache*28433+1)%digit_save
    print "Result: {}".format(cache)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
