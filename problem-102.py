#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime

# http://www.cnblogs.com/graphics/archive/2010/08/05/1793393.html
# http://blackpawn.com/texts/pointinpoly/default.html
@runTime
def byMagic():
    axis = [map(int, l.split(",")) for l in open("p102_triangles.txt").readlines()]


    print "Result: {}".format()


if __name__ == "__main__":
    bruteForce()
