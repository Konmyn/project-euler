#!/usr/bin/python
# -*- coding: utf-8 -*-


def load_data():
    with open('p022_names.txt') as doc:
        datas = doc.read().strip('"').split('","')
        datas.sort()
    return datas

def main():
    index = 1
    score = 0
    names = load_data()
    for name in names:
        char_sum = 0
        for char in name:
            char_sum += ord(char)-64
        score += char_sum*index
        index += 1
    print score


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
