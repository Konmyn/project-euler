#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


@runTime
def bruteForce():
    # best choice remember re
    re = [0, []]
    # http://music.hujiang.com/music/163596/
    words = ['the', 'be', 'to', 'of', 'and', 'in', 'that', 'it', 'for', 'not']
    # chr(97) is 'a', chr(65) is 'A'
    codes = map(int, open("p059_cipher.txt").readline().split(","))
    for p1 in xrange(97, 123):
        for p2 in xrange(97, 123):
            for p3 in xrange(97, 123):
                cp = codes[:]
                cp[::3] = [p1^i for i in cp[::3]]
                cp[1::3] = [p2^i for i in cp[1::3]]
                cp[2::3] = [p3^i for i in cp[2::3]]
                s = ''.join(map(chr, cp))
                count = 0
                for word in words:
                    if word in s:
                        count += 1
                if count>re[0]:
                    re = [count, cp]
    print "Result: {}".format(sum(re[1]))

@runTime
def singleBruteForce():
    word = ' the '
    codes = map(int, open("p059_cipher.txt").readline().split(","))
    for p1 in xrange(97, 123):
        for p2 in xrange(97, 123):
            for p3 in xrange(97, 123):
                cp = codes[:]
                cp[::3] = [p1^i for i in cp[::3]]
                cp[1::3] = [p2^i for i in cp[1::3]]
                cp[2::3] = [p3^i for i in cp[2::3]]
                s = ''.join(map(chr, cp))
                if word in s:
                    print "Result: {}".format(sum(cp))
                    return

if __name__ == "__main__":
    bruteForce()
    singleBruteForce()
