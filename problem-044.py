#!/usr/bin/python
# -*- coding: utf-8 -*-


def pentagonal_list(upper_limit):
    return [x * (3 * x - 1) / 2 for x in xrange(1, upper_limit + 1)]


def main():
    upper_limit = 6000
    pen_list = pentagonal_list(upper_limit)
    result_list = []
    j = 2
    while j < upper_limit:
        i = 0
        while i < upper_limit - j:
            if not (pen_list[i] + pen_list[i + j]) % 2 and not (pen_list[i + j] - pen_list[i]) % 2:
                if (pen_list[i] + pen_list[i + j]) / 2 in pen_list[i + j:] and (pen_list[i + j] - pen_list[i]) / 2 in pen_list[:i + j]:
                    result_list.append([pen_list[i], pen_list[i + j]])
            i += 1
        j += 1
    print "Result: {} -> {}".format(upper_limit, result_list)
Result: 6000 -> []
Time used(s): 300.045874119


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
