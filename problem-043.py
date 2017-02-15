#!/usr/bin/python
# -*- coding: utf-8 -*-


from itertools import permutations
from tools.runningTime import runTime


def check_property(num_tuple):
    nt = num_tuple
    # if (nt[1]*100+nt[2]*10+nt[3])%2:
    #     return False
    if (nt[2]+nt[3]+nt[4])%3:
        return False
    # if (nt[3]*100+nt[4]*10+nt[5])%5:
    #     return False
    if (nt[4]*100+nt[5]*10+nt[6])%7:
        return False
    if (nt[5]*100+nt[6]*10+nt[7])%11:
        return False
    if (nt[6]*100+nt[7]*10+nt[8])%13:
        return False
    if (nt[7]*100+nt[8]*10+nt[9])%17:
        return False
    return True

def check_property_by_list(nt):
    for i, j in enumerate([2, 3, 5, 7, 11, 13, 17]):
        if reduce(lambda x, y: 10*x+y, nt[i+1:i+4], 0)%j:
            return False
    return True

def check_property_by_number(number):
    for i, j in enumerate([2, 3, 5, 7, 11, 13, 17]):
        if int(str(number)[i+1:i+4])%j:
            return False
    return True

@runTime
def byPermutation():
    result_list = []
    for perm in permutations(range(10)):
        if perm[0] == 0 or perm[3]%2 or perm[5]%5:
            continue
        if check_property(perm):
        # if check_property_by_list(perm):
            number = reduce(lambda x, y: 10*x+y, perm, 0)
        # number = reduce(lambda x, y: 10*x+y, perm, 0)
        # if check_property_by_number(number):
            result_list.append(number)
    # print result_list
    print "Result: {}".format(sum(result_list))


if __name__ == "__main__":
    byPermutation()
