#!/usr/bin/python
# -*- coding: utf-8 -*-


LENGTH = 21

def array_generate():
    a_list = [0]*LENGTH
    array = []
    for i in range(LENGTH):
        array.append(a_list[:])
    return array

def main():
    array = array_generate()
    for i in range(LENGTH):
        array[0][i] = 1
        array[i][0] = 1
    for i in range(1, LENGTH):
        for j in range(1, LENGTH):
            array[i][j] = array[i-1][j] + array[i][j-1]
    print "Result: {}".format(array[LENGTH-1][LENGTH-1])

if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
