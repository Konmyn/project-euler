#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime



def array_format(strings):
    array = strings[:].strip().split('\n')
    array_list = []
    for i in array:
        array_list.append([int(j) for j in i.split()])
    return array_list


def max_product_horizontal(array):
    max_pr = 0
    for i in array:
        j = 0
        while j < 17:
            max_pr = max(max_pr, reduce(lambda x, y: x * y, i[j:j + 4], 1))
            j += 1
    return max_pr


def max_product_vertical(array):
    max_pr = i = 0
    while i < 20:
        j = 0
        while j < 17:
            temp_array = [array[j][i], array[j + 1][i], array[j + 2][i], array[j + 3][i]]
            max_pr = max(max_pr, reduce(lambda x, y: x * y, temp_array, 1))
            j += 1
        i += 1
    return max_pr


# diagonal from up-left to down-right
def max_product_diagonal_1(array):
    max_pr = i = 0
    while i < 17:
        j = 0
        while j < 17:
            temp_array = [array[j][i], array[j + 1][i + 1], array[j + 2][i + 2], array[j + 3][i + 3]]
            max_pr = max(max_pr, reduce(lambda x, y: x * y, temp_array, 1))
            j += 1
        i += 1
    return max_pr


# diagonal from up-right to down-left
def max_product_diagonal_2(array):
    max_pr = i = 3
    while i < 20:
        j = 0
        while j < 17:
            temp_array = [array[j][i], array[j + 1][i - 1], array[j + 2][i - 2], array[j + 3][i - 3]]
            max_pr = max(max_pr, reduce(lambda x, y: x * y, temp_array, 1))
            j += 1
        i += 1
    return max_pr


def main():
    array = array_format(ARRAY)
    max_pr = max(max_product_horizontal(array), max_product_vertical(array),
                 max_product_diagonal_1(array), max_product_diagonal_2(array))
    print "Result: {}".format(max_pr)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
