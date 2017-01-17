#!/usr/bin/python
# -*- coding: utf-8 -*-


TRIANGLE =\
'''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

def array_text_to_number():
    number_array = []
    text_array = [j.split() for j in TRIANGLE.split("\n")]
    for text in text_array:
        number_array.append([int(i) for i in text])
    return number_array

def main():
    array = array_text_to_number()
    triangle_height = len(array)
    max_path = [0]*triangle_height
    max_path[0] = array[0][0]
    for m in range(1, triangle_height):
        i = 0
        copy_list = max_path[:]
        while i < len(array[m]):
            if i == 0:
                max_path[i] = copy_list[i] + array[m][i]
            elif i == len(array[m])-1:
                max_path[i] = copy_list[i-1] + array[m][i]
            else:
                max_path[i] = max(copy_list[i] + array[m][i], copy_list[i-1] + array[m][i])
            i += 1
    print max(max_path)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
