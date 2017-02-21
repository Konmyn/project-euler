#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

def pokerAnalysis(hands):
    r = [0]*10
    cache = []
    p1ss = True if len(set([i[1] for i in hands]))==1 else False
    for v in [i[0] for i in hands]:
        cache.append(pv.index(v))
    cache.sort()
    buffer = [0]*13
    for v in [i[0] for i in hands]:
        buffer[pv.index(v)] += 1
    if p1ss:
        r[5]=6 # Flush
    if cache[-1]-cache[0] == 4 and len(set(cache))==5:
        r[4]=5 # Straight
        if r[5]:
            r[8] = 9 # Straight Flush
        if cache[-1]==12:
            r[9] = 10 # Royal Flush
        return (r, [cache[-1]])
    if len(set(cache))==2:
        if 4 in buffer:
            r[7] = 8 # Four of a Kind
            return (r, [buffer.index(4), buffer.index(1)])
        else:
            r[6] = 7 # Full House
            return (r, [buffer.index(3), buffer.index(2)])
    if len(set(cache))==3:
        if 3 in buffer:
            mem = cache[:]
            mem.remove(buffer.index(3))
            mem.remove(buffer.index(3))
            mem.remove(buffer.index(3))
            r[3] = 4 # Three of a Kind
            return (r, [buffer.index(3)]+mem[::-1])
        else:
            r[2] = 3 # Two Pairs
            return (r, [12 - buffer[::-1].index(2), buffer.index(2), buffer.index(1)])
    if len(set(cache))==4:
        mem = cache[:]
        mem.remove(buffer.index(2))
        mem.remove(buffer.index(2))
        r[1] = 2 # One Pair
        return (r,[buffer.index(2)]+mem[::-1])
    else:
        r[0] = 1 # High Card
        return (r, cache[::-1])

# poker values in order
pv = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
# poker color
pc = ['C', 'D', 'H', 'S']
def is_player1_wins(poker):
    p1, p2 = pokerAnalysis(poker[:5]), pokerAnalysis(poker[5:])
    print p1, p2


@runTime
def brute_force_method(uplimit=10**3):
    pw = 0  #player 1 wins counter, initalize to 0.
    pokers = [i.rstrip().split() for i in open("p054_poker.txt").readlines()]
    for poker in pokers[:5]:
        pw += 1 if is_player1_wins(poker) else 0
    print "Result: {}".format(pw)


if __name__ == "__main__":
    brute_force_method()
