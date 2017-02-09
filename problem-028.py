#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


def generate_diagonal(edge_length):
    round_end = 1
    edge = 1
    step = edge-1
    while edge <= edge_length:
        yield [round_end, round_end-step, round_end-step*2, round_end-step*3]
        edge += 2
        step = edge-1
        round_end += step*4

@runTime
def bruteForce(edge=1001):
    if edge == 1:
        print "Result: 1"
        return
    print "Result: {}".format(sum(map(sum, generate_diagonal(edge)))-3)

# https://en.wikipedia.org/wiki/Summation#Some_summations_of_polynomial_expressions
# https://www.hackerrank.com/contests/projecteuler/challenges/euler028
@runTime
def byFormula(edge=1001):
    s = (edge-1)/2
    print "Result: {}".format((16*s*s*s + 30*s*s + 26*s + 3)/3)


if __name__ == "__main__":
    bruteForce()
    byFormula()
