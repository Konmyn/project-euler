#!/usr/bin/python
# -*- coding: utf-8 -*-


LIST_XY = []

def load_data():
    datas = []
    with open('p082_matrix.txt') as doc:
        for line in doc:
            datas.append([int(number) for number in line.strip().split(',')])
    return datas

def main():
    LIST_XY =load_data()
    print "Result: {}".format()


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
