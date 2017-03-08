#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


# 最短公共超序列问题(Shortest common supersquence)
# Hamilton路问题
# http://bookshadow.com/weblog/2016/10/30/leetcode-sequence-reconstruction/
# 两个生物序列最短公共超序列的动态规划算法
def SCSS(la, lb):
    lena, lenb = len(la)+1, len(lb)+1
    array = [[0]*lena for i in xrange(lenb)]
    for i in xrange(lena):
        array[0][i] = i
    for j in xrange(lenb):
        array[j][0] = j
    for i in xrange(1, lena):
        for j in xrange(1, lenb):
            array[j][i] = min(array[j-1][i]+1,
                              array[j][i-1]+1,
                              array[j-1][i-1]+(1 if la[j-1]==lb[i-1] else 2))
    print array


@runTime
def byMagic():
    axis = [map(int, l.split(",")) for l in open("p102_triangles.txt").readlines()]


    print "Result: {}".format()


if __name__ == "__main__":
    SCSS([1,2,3], [4,5,6])
