#!/usr/bin/python
# -*- coding: utf-8 -*-


import re
from tools.runningTime import runTime
from tools.common import is_prime


def is_truncatable_prime(n, pset):
    from_right = n//10
    while from_right:
        if from_right not in pset:
            return False
        from_right //= 10
    num_len = len(str(n)) - 1
    from_left = n%(10**num_len)
    num_len -= 1
    while from_left:
        if from_left not in pset:
            return False
        from_left %= 10**num_len
        num_len -= 1
    return True

@runTime
def bruteForce():
    n = 11
    prime = set([2, 3, 5, 7])
    target_list = []
    while len(target_list) < 11:
        if is_prime(n):
            prime.add(n)
            if is_truncatable_prime(n, prime):
                target_list.append(n)
        n += 2
    print target_list
    print "Result: {}".format(sum(target_list))

def is_trunc(n):
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:i])):
            return False
    return True

@runTime
def newBruteForce():
    n, f = 11, 1
    tl = []
    while len(tl)<11:
        n += 3-f
        f = -f
        if not (n>100 and re.search('245680', str(n))):
            if is_prime(n) and is_trunc(n):
                tl.append(n)
    print "Result: {}".format(sum(tl))

# only if you know the uplimit is less than something like one million.
# not read this function yet.
@runTime
def problem37():
    l, m = (1000000 - 1)/2, int((1000000 ** 0.5)//1 - 1)/2
    a, e, z = [True] * l, ['2', '0', '4', '6', '8'], 23
    for i in xrange(m):
        if a[i]:
            s = i + i + 3
            t = (s ** 2)/2 - 1
            for j in xrange(t, l, s):
               a[j] = False
    for x in xrange(10, l):
        if a[x]:
            p, b = 2 * x + 3, True
            for d in str(p)[1:]:
                if d in e:
                    b = False
                    break
            if b and str(p)[0] in e[2:] or str(p)[0] == '1' or str(p)[-1] == '1': b = False
            if b:
                for i in xrange(1, len(str(p))):
                    q = (int(str(p)[i:]) - 3)/2
                    r = (int(str(p)[:i]) - 3)/2
                    if not a[q] or not a[r]:
                        b = False
                        break
                if b: z += p
    print "Result: {}".format(z)

if __name__ == "__main__":
    bruteForce()
    newBruteForce()
    problem37()
