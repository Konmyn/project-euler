#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/#!
# https://www.codechef.com/wiki/tutorial-dynamic-programming


from random import randint


# http://blog.dreamshire.com/project/dyn_prog.pdf
def minCoinSolution(coins, target):
    solution = [float('inf')]*(target+1)

    solution[0] = 0
    for i in xrange(target+1):
        for j in xrange(len(coins)):
            # if coins[j]<=i and solution[i-coins[j]]+1<solution[i]:
            #     solution[i] = solution[i-coins[j]]+1
            if coins[j]<=i:
                solution[i] = min(solution[i-coins[j]]+1, solution[i])

    print solution[target]

def minCoinSolution2(coins, target):
    solution = [float('inf')]*(target+1)

    solution[0] = 0
    for i in xrange(len(coins)):
        # index transforming, think again
        for j in xrange(target+1-coins[i]):
            solution[j+coins[i]] = min(solution[j+coins[i]], solution[j]+1)

    print solution[target]

# https://projecteuler.net/problem=31
# http://www.algorithmist.com/index.php/Coin_Change
def coinSolutionCounter(n, m, mem):
    if n<0 or m<0:
        return 0
    elif n==0:
        return 1
    elif mem[n-1][m-1]:
        return mem[n-1][m-1]
    else:
        mem[n-1][m-1] = coinSolutionCounter(n, m-1, mem)+coinSolutionCounter(n-S[m], m, mem)
        return mem[n-1][m-1]

# https://projecteuler.net/problem=76
def integerPartition(n, m, mem):
    if n<0 or m<0:
        return 0
    elif n==0:
        return 1
    elif mem[n-1][m-1]:
        return mem[n-1][m-1]
    else:
        mem[n-1][m-1] = integerPartition(n, m-1, mem)+integerPartition(n-I[m], m, mem)
        return mem[n-1][m-1]

# generate random integer in [begin, end] items counts=length.
def generateRandomList(begin=1, end=10, length=10):
    return [randint(begin, end) for i in range(length)]

def longestNonDecreasingSequence(seq):
    L = len(seq)
    result = [1]*L

    for i in xrange(L):
        for j in xrange(i):
            if seq[i]>=seq[j]:
                result[i] = max(result[i], result[j]+1)

    print seq
    print result

# generate random integer N rows M columns array in range [begin, end].
def generateRandomArray(N=10, M=20, begin=1, end=20):
    return [[randint(begin, end) for i in xrange(M)] for j in xrange(N)]

def maximumNumberOfApples(array):
    N, M = len(array), len(array[0])
    S = [[0]*M for i in xrange(N)]

    for i in xrange(N):
        for j in xrange(M):
            S[i][j] = array[i][j] + max(S[i-1][j] if i>0 else 0, S[i][j-1] if j>0 else 0)

    print array
    print S

# Minimum Steps to One
# Memoization solutions, Top-Down
def getMinSteps(n, mem):
    if n==1:
        return 0
    elif mem[n-1] != -1:
        return mem[n-1]
    r = min(1+getMinSteps(n-1, mem),
            1+getMinSteps(n/2, mem) if n%2==0 else float('inf'),
            1+getMinSteps(n/3, mem) if n%3==0 else float('inf'))
    mem[n-1] = r
    return r

# DP, Bottom-Up
def getMinSteps2(n):
    S = [0]*n
    for i in xrange(1, n):
        S[i] = min(S[i-1]+1, S[(i+1)/2-1]+1 if (i+1)%2==0 else float('inf'),
                   S[(i+1)/3-1]+1 if (i+1)%3==0 else float('inf'))
    return S[-1]

if __name__ == "__main__":
# min coin counter problem:

    # q = [
    # [[1, 2, 5, 10, 20, 50, 100, 200], 200],
    # [[1, 3, 5], 11]
    # ]
    # for i in q:
    #     minCoinSolution(*i)
    #     minCoinSolution2(*i)

# finding the number of ways of making changes for a particular amount of cents.
    # S = [1, 2, 5, 10, 20, 50, 100, 200]
    # n, m = 200, len(S)-1
    # mem = [[0]*m for i in xrange(n)]
    # print coinSolutionCounter(n, m, mem)

# Integer Partition
    # summation = 100
    # I = range(1, summation)
    # n, m = summation, summation-2
    # mem = [[0]*m for i in xrange(n)]
    # print integerPartition(n, m, mem)


# longest non-decreasing sequence.

    # longestNonDecreasingSequence(generateRandomList())
    # longestNonDecreasingSequence([5, 3, 4, 8, 6, 7])

# bi-dimensional DP problems

    # maximumNumberOfApples(generateRandomArray(3, 3))

# Minimum Steps to One
    # when n = 1000, RuntimeError: maximum recursion depth exceeded
    n = 3**10
    # mem = [-1]*n
    # print getMinSteps(n, mem)
    # print mem
    print getMinSteps2(n)
