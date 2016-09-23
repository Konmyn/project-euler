#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_perfect_square(n):
    return pow(int(pow(n, 0.5)), 2) == n


def main():
    # x, y, z
    # i, j, k,
    i = 3
    while i:
        square_i = i ** 2
        j = 2
        while j < i:
            square_j = j ** 2
            k = 1
            while k < j:
                square_k = k ** 2
                if is_perfect_square(square_i - square_k):
                    if is_perfect_square(square_j - square_k):
                        if is_perfect_square(square_i - square_j):
                            if not (square_i + square_j - square_k) % 2 and not (square_i + square_k - square_j) % 2 and not (square_k + square_j - square_i) % 2:
                                result = (square_i + square_j + square_k) / 2
                                x = (square_i + square_j - square_k) / 2
                                y = (square_i + square_k - square_j) / 2
                                z = (square_k + square_j - square_i) / 2
                                if x > y > z > 0:
                                    print x, y, z, result
                                    print "Result: {}".format(result)
                                    return
                k += 1
            j += 1
        i += 1


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)

# Result: 1006193
# Time used(s): 93.5784039497
