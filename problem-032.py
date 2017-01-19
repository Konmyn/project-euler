#!/usr/bin/python
# -*- coding: utf-8 -*-


from itertools import permutations


def main():
    products = set()
    perm = permutations(range(1,10))
    while True:
        try:
            i = perm.next()
            if (i[0]*10+i[1])*(i[2]*100+i[3]*10+i[4]) == i[5]*1000+i[6]*100+i[7]*10+i[8]:
                products.add(i[5]*1000+i[6]*100+i[7]*10+i[8])
            if i[0]*(i[1]*1000+i[2]*100+i[3]*10+i[4]) == i[5]*1000+i[6]*100+i[7]*10+i[8]:
                products.add(i[5]*1000+i[6]*100+i[7]*10+i[8])
        except StopIteration:
            break
    print products
    print "Result: {}".format(sum(products))


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
