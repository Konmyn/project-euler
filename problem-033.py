#!/usr/bin/python
# -*- coding: utf-8 -*-


import fractions


def main():
    n_t = []
    nomi = 11
    while nomi <= 98:
        denomi = nomi%10*10+nomi//10
        while denomi%10 and denomi>nomi:
            if denomi%10*nomi == nomi//10*denomi:
                n_t.append((nomi, denomi, nomi//10, denomi%10))
            denomi += 1
        nomi += 1
    no_pro = reduce(lambda x, y: x*y, [i[2] for i in n_t], 1)
    de_pro = reduce(lambda x, y: x*y, [i[3] for i in n_t], 1)
    gcd = fractions.gcd(no_pro, de_pro)
    print "Result: {}".format(de_pro//gcd)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
