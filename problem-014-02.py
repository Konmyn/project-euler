#!/usr/bin/python
# -*- coding: utf-8 -*-


# backward method, just for test, not solution.
def main():
    number = 1
    _dict = {number: [1]}
    while number < 30:
        list_nu = number + 1
        _dict[list_nu] = []
        for i in _dict[number]:
            if not i % 2 and i != 1 and ((i - 1) / 3) % 2 and i != 4 and not (i - 1) % 3:
                _dict[list_nu].append((i - 1) / 3)
            _dict[list_nu].append(i * 2)
        number = list_nu
    for i in _dict.itervalues():
        print min(i)
    # print "Result: {} has longest chain {}".format(target, max_length)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
