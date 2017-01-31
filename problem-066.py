#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    D = 1
    square_number = [x**2 for x in range(1,int(1000**0.5)+1)]
    print square_number
    largest_value = 0
    D_to_get_largest_value = 0
    while D <= 1000:
        if D in square_number:
            D += 1
            continue
        x = 1
        break_loopx = False
        while True:
            y = 1
            while (x**2 - (y**2)*D) > 0:
                if (x**2 - (y**2)*D) == 1:
                    if largest_value < x:
                        largest_value = x
                        D_to_get_largest_value = D
                    break_loopx = True
                    print largest_value, D_to_get_largest_value
                    break
                y += 1
            if break_loopx:
                break
            x += 1
        D += 1
    print "Result: {}".format(D_to_get_largest_value)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
