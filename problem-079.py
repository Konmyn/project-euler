#!/usr/bin/python
# -*- coding: utf-8 -*-


from itertools import permutations
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

def check_keys(ilist, olist):
    for key in olist:
        cache = -1
        for k in key:
            if cache > ilist.index(k):
                return False
            cache = ilist.index(k)
    return True

# this problem is some kind of cheating. "Think it simple!"
@runTime
def bruteForce():
    keys = [map(int, [i for i in l]) for l in open("p079_keylog.txt").read().split()]
    # assume that there is no repeating in digits.
    a = set()
    for key in keys:
        for i in key:
            a.add(i)
    digits = list(a)
    # digits = [0, 1, 2, 3, 6, 7, 8, 9]
    for nlist in permutations(digits):
        if check_keys(nlist, keys):
            print "Result: {}".format(''.join(map(str, nlist)))
            return


if __name__ == "__main__":
    bruteForce()
