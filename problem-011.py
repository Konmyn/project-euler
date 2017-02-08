#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


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

@runTime
def on_my_thoughts():
    grid = [map(int, l.rstrip().split()) for l in open("p011_grid.txt").readlines()]
    max_pr = max(max_product_horizontal(grid), max_product_vertical(grid),
                 max_product_diagonal_1(grid), max_product_diagonal_2(grid))
    print "Result: {}".format(max_pr)

@runTime
def integreted():
    target = 0
    g = [map(int, l.rstrip().split()) for l in open("p011_grid.txt").readlines()]
    rows, cols, size = len(g), len(g[0]), 4
    for i in xrange(rows):
        for j in xrange(cols-size+1):
            phv = max(g[i][j] * g[i][j+1] * g[i][j+2] * g[i][j+3],
                      g[j][i] * g[j+1][i] * g[j+2][i] * g[j+3][i])
            if i<rows-size:
                pdd = max(g[i][j] * g[i+1][j+1] * g[i+2][j+2] * g[i+3][j+3],
                          g[i+3][j] * g[i+2][j+1] * g[i+1][j+2] * g[i][j+3])
        target = max(target, phv, pdd)
    print "Result: {}".format(target)


if __name__ == "__main__":
    on_my_thoughts()
    integreted()
