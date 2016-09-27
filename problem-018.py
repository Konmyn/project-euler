#!/usr/bin/python
# -*- coding: utf-8 -*-


TRIANGLE =\
'''
75
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
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''


def data_format():
    rows = 15
    # columns = 15
    array = []
    for i in range(1, rows+1):
        n = 0
        step = sum(range(i))
        internal = []
        while n < i:
            internal.append(int(series[n*3+3*step:3*n+3*step+2]))
            n += 1
        array.append(internal)
    return array

target = 0
aim = getserial()
move = m = n = 0
while m < 15:
    move = move + aim[m][n]
    m += 1


def main():
    fib_stop = 4000000
    a = 1
    b = 2
    c = a + b
    target_list = [2]
    while c <= fib_stop:
        c = a + b
        if not c % 2:
            target_list.append(c)
        a = b
        b = c
    print "Result: {}".format(sum(target_list))


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
