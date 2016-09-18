#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    n = 1
    target_list = []
    while n < 1000:
        if not n % 3:
            target_list.append(n)
        elif not n % 5:
            target_list.append(n)
        n += 1
    print "Result: {}".format(sum(target_list))


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)

if False:
    # one line solution below:
    print sum([x for x in xrange(1000) if not x % 3 or not x % 5])
