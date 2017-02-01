#!/usr/bin/python
# -*- coding: utf-8 -*-


from decimal import *


LIST_EXP = []

def load_data():
    datas = []
    with open('p099_base_exp.txt') as doc:
        for line in doc:
            datas.append(line.strip().split(','))
    return datas

def main():
    LIST_EXP =load_data()
    max_num = 0
    loop = len(LIST_EXP)
    for i in range(loop):
        cache = Decimal(LIST_EXP[i][0]).log10()*Decimal(LIST_EXP[i][1])
        if max_num < cache:
            max_num = cache
            row_number = i+1
    print "Result: {}".format(row_number)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
