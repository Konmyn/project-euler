#!/usr/bin/python
# -*- coding: utf-8 -*-


from collections import Counter
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

# This is a shit misleading question for i am not a good poker player!
# how to deal with A,2,3,4,5?!
def pokerAnalysis(hands):
    r = [0]*10 # poker hands rank
    c = [0]*13 # value counter list
    z = [] # value list in order
    pss = True if len(set([i[1] for i in hands]))==1 else False #palyer same suit
    for v in [i[0] for i in hands]:
        z.append(pv.index(v))
        c[pv.index(v)] += 1
    z.sort()
    if pss:
        # print hands
        r[5]=6 # Flush
    if z[-1]-z[0] == 4 and len(set(z))==5:
        r[4]=5 # Straight
        # print hands
        if r[5]:
            if z[-1]==12:
                r[9] = 10 # Royal Flush
            else:
                r[8] = 9 # Straight Flush
            return (r, z[::-1])
    if len(set(z))==2:
        if 4 in c:
            # print hands
            r[7] = 8 # Four of a Kind
            return (r, [c.index(4), c.index(1)])
        else:
            # print hands
            r[6] = 7 # Full House
            return (r, [c.index(3), c.index(2)])
    if len(set(z))==3:
        if 3 in c:
            # print hands
            # print z
            # print c
            mem = z[:]
            mem.remove(c.index(3))
            mem.remove(c.index(3))
            mem.remove(c.index(3))
            r[3] = 4 # Three of a Kind
            # print (r, [c.index(3)]+mem[::-1])
            return (r, [c.index(3)]+mem[::-1])
        else:
            r[2] = 3 # Two Pairs
            return (r, [12 - c[::-1].index(2), c.index(2), c.index(1)])
    if len(set(z))==4:
        mem = z[:]
        mem.remove(c.index(2))
        mem.remove(c.index(2))
        r[1] = 2 # One Pair
        return (r,[c.index(2)]+mem[::-1])
    else:
        r[0] = 1 # High Card
        return (r, z[::-1])

# poker values in order
pv = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
# poker color
pc = ['C', 'D', 'H', 'S']
def is_player1_wins(poker):
    p1, p2 = pokerAnalysis(poker[:5]), pokerAnalysis(poker[5:])
    # print p1, '\n', p2
    if max(p1[0])>max(p2[0]):
        return True
    elif max(p1[0])<max(p2[0]):
        print poker, '\n',p1, '\n', p2
        return False
    else:
        for i in range(len(p1[1])):
            if p1[1][i]>p2[1][i]:
                return True
        return False

@runTime
def brute_force_method(uplimit=10**3):
    pw = 0  #player 1 wins counter, initalize to 0.
    pokers = [i.split() for i in open("p054_poker.txt")]
    for poker in pokers:
        pw += 1 if is_player1_wins(poker) else 0
    print "Result: {}".format(pw)

@runTime
def trick():
    hands = (line.split() for line in open("p054_poker.txt"))

    values = {r:i for i,r in enumerate('23456789TJQKA', start=2)}
    straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
    ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]

    def hand_rank(hand):
        score = zip(*sorted(((v, values[k]) for k,v in Counter(x[0] for x in hand).items()), reverse=True))
        score[0] = ranks.index(score[0])
        if len(set(card[1] for card in hand)) == 1: score[0] = 5  # flush
        if score[1] in straights: score[0] = 8 if score[0] == 5 else 4  # str./str. flush
        return score

    print "Project Euler 54 Solution =", sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands)


if __name__ == "__main__":
    # brute_force_method()
    trick()
