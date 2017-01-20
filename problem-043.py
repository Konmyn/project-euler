#!/usr/bin/python
# -*- coding: utf-8 -*-


from itertools import permutations

def check_property(num_tuple):
    nt = num_tuple
    if (nt[1]*100+nt[2]*10+nt[3])%2 != 0:
        return False
    if (nt[2]*100+nt[3]*10+nt[4])%3 != 0:
        return False
    if (nt[3]*100+nt[4]*10+nt[5])%5 != 0:
        return False
    if (nt[4]*100+nt[5]*10+nt[6])%7 != 0:
        return False
    if (nt[5]*100+nt[6]*10+nt[7])%11 != 0:
        return False
    if (nt[6]*100+nt[7]*10+nt[8])%13 != 0:
        return False
    if (nt[7]*100+nt[8]*10+nt[9])%17 != 0:
        return False
    return True

def concatenate_tuple(num_tuple):
    number = 0
    for n in num_tuple:
        number = number*10 + n
    return number

def main():
    result_list = []
    perm = permutations(range(10))
    while True:
        try:
            num_tuple = perm.next()
            if num_tuple[0] == 0:
                continue
            if check_property(num_tuple):
                number = concatenate_tuple(num_tuple)
                result_list.append(number)
        except StopIteration:
            break
    print "Result: {}".format(sum(result_list))


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
