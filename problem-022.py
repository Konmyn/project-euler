#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


def load_data():
    with open('p022_names.txt') as doc:
        datas = doc.read().strip('"').split('","')
        datas.sort()
    return datas

@runTime
def on_my_own():
    index, score, names = 1, 0, load_data()
    for name in names:
        char_sum = 0
        for char in name:
            char_sum += ord(char)-64
        score += char_sum*index
        index += 1
    print "Result: {}".format(score)

@runTime
def same_way():
    names = sorted(open('p022_names.txt').read().split(','))
    s = 0
    for index, name in enumerate(names):
        s += (index+1)*sum(ord(c)-64 for c in name.strip('"'))
    print "Result: {}".format(s)


if __name__ == "__main__":
    on_my_own()
    same_way()
