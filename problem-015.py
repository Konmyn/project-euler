#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import factorial as f


def grid_generate(edge=20):
    row = [0]*(edge+1)
    grid = []
    for i in xrange(edge+1):
        grid.append(row[:])
    return grid

@runTime
def on_my_own(edge=20):
    grid = grid_generate(edge)
    for i in xrange(edge+1):
        grid[0][i] = 1
        grid[i][0] = 1
    for i in xrange(1, edge+1):
        for j in xrange(1, edge+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    print "Result: {}".format(grid[edge][edge])

# Pascal's triangle
# https://en.wikipedia.org/wiki/Pascal's_triangle
# Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2
# https://oeis.org/A000984
# Catalan number
# https://en.wikipedia.org/wiki/Catalan_number
@runTime
def by_formula(eh=20, ev=20):
    print "Result: {}".format(f(eh+ev)/f(eh)/f(ev))

if __name__ == "__main__":
    on_my_own()
    by_formula()
