#!/usr/bin/python
# -*- coding: utf-8 -*-


from operator import add
from math import sqrt
from tools.runningTime import runTime


# store triangle as a list, the first elements is the number n
# that generates the last triangle number in list.
TRIANGLE_NUM_LIST = [1, 1]

def is_triangle_number(number):
    global TRIANGLE_NUM_LIST
    if number in TRIANGLE_NUM_LIST[1:]:
        return True
    elif number<TRIANGLE_NUM_LIST[-1]:
        return False
    else:
        while number>TRIANGLE_NUM_LIST[-1]:
            TRIANGLE_NUM_LIST[0] += 1
            TRIANGLE_NUM_LIST.append(TRIANGLE_NUM_LIST[0]*(TRIANGLE_NUM_LIST[0]+1)/2)
        return TRIANGLE_NUM_LIST[-1] == number

@runTime
def bruteForce():
    global TRIANGLE_NUM_LIST
    words = [w.strip('"') for w in open('p042_words.txt').read().split(',')]
    counter = 0
    for word in words:
        if is_triangle_number(reduce(add, [ord(c)-64 for c in word], 0)):
            counter += 1
    # print TRIANGLE_NUM_LIST
    print "Result: {}".format(counter)

def is_triangle(n):
    return not bool((sqrt(8*n+1)-1)/2%1)

def score(word):
    return sum(ord(letter)-64 for letter in word)

@runTime
def newBruteForce():
    words = [w[1:-1] for w in open('p042_words.txt').read().split(',')]
    print "Result: {}".format(sum(is_triangle(score(w)) for w in words))


if __name__ == "__main__":
    bruteForce()
    newBruteForce()
