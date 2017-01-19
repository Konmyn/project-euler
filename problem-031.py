#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    n200 = 0
    counter = 0
    while n200<=1:
        n100 = 0
        while n100<=2:
            n50 = 0
            while n50<=4:
                n20 = 0
                while n20<=10:
                    n10 = 0
                    while n10<=20:
                        n5 = 0
                        while n5<=40:
                            n2 = 0
                            while n2<=100:
                                n1 = 0
                                while n1<=200:
                                    if (n200*200+n100*100+n50*50+n20*20+n10*10+n5*5+n2*2+n1*1) == 200:
                                        counter += 1
                                    if (n200*200+n100*100+n50*50+n20*20+n10*10+n5*5+n2*2+n1*1) > 200:
                                        break
                                    n1 += 1
                                n2 += 1
                            n5 += 1
                        n10 += 1
                    n20 += 1
                n50 += 1
            n100 += 1
        n200 += 1
    print "Result: {}".format(counter)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
