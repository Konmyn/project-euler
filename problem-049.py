#!/usr/bin/python
# -*- coding: utf-8 -*-


from operator import add
from tools.runningTime import runTime
from tools.common import is_prime, is_perm


def gen_prime_list(start=1001, stop=9999):
    PRIME_LIST = []
    for number in xrange(start, stop+1, 2):
        if is_prime(number):
            PRIME_LIST.append(number)
    for i in [1487, 4817, 8147]:
        PRIME_LIST.remove(i)
    return PRIME_LIST

def is_permutation(x, y, z):
    a = [0]*10
    b = [0]*10
    c = [0]*10
    while x:
        a[x%10] += 1
        x //= 10
    while y:
        b[y%10] += 1
        y //= 10
    while z:
        c[z%10] += 1
        z //= 10
    if a == b == c:
        return True
    else:
        return False

@runTime
def bruteForce():
    PRIME_LIST = gen_prime_list()
    for i in xrange(len(PRIME_LIST)-1, 1, -1):
        for j in xrange(i-1, 0, -1):
            diff = PRIME_LIST[j]*2-PRIME_LIST[i]
            if diff in PRIME_LIST[:j] and is_permutation(diff, PRIME_LIST[j], PRIME_LIST[i]):
                target = [diff, PRIME_LIST[j], PRIME_LIST[i]]
                print "Result: {}".format(reduce(add, [str(i) for i in target]))
                return

# this problem is not very clearly descripted.
@runTime
def newBruteForce():
    n = 1489
    while not (is_prime(n) and is_prime(n+3330) and is_prime(n+6660) and\
              is_perm(n, n+3330) and is_perm(n, n+6660)):
          n += 2
    print "Result: {}".format(str(n)+str(n+3330)+str(n+6660))


if __name__ == "__main__":
    bruteForce()
    newBruteForce()
