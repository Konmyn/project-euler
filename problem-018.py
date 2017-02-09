#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


@runTime
def my_greed_method():
    array = [map(int, l.split()) for l in open('p018_triangle.txt').readlines()]
    triangle_height = len(array)
    max_path = [0]*triangle_height
    max_path[0] = array[0][0]
    for m in xrange(1, triangle_height):
        copy_list = max_path[:]
        for i in xrange(len(array[m])):
            if i == 0:
                max_path[i] = copy_list[i] + array[m][i]
            elif i == len(array[m])-1:
                max_path[i] = copy_list[i-1] + array[m][i]
            else:
                max_path[i] = max(copy_list[i]+array[m][i], copy_list[i-1]+array[m][i])
    print "Result: {}".format(max(max_path))

@runTime
def down_to_top():
    table = [map(int, s.split()) for s in open('p018_triangle.txt').readlines()]
    for row in xrange(len(table)-1, 0, -1):
        for col in xrange(0, row):
            table[row-1][col] += max(table[row][col], table[row][col+1])
    print "Result: {}".format(table[0][0])


if __name__ == "__main__":
    my_greed_method()
    down_to_top()
