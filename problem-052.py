#!/usr/bin/python
# -*- coding: utf-8 -*-


def contain_same_digits(n):
    counter = [0]*10
    cache = n
    while cache:
        counter[cache%10] += 1
        cache //= 10
    for i in range(2, 7):
        cache = n*i
        counteri = [0]*10
        while cache:
            counteri[cache%10] += 1
            cache //= 10
        if counter != counteri:
            return False
    return True

def main():
    power = 1
    while True:
        natural = pow(10, power)
        limit = int((1+2.0/3)*pow(10, power))
        while natural<=limit:
            if contain_same_digits(natural):
                print "Result: {}".format(natural)
                return
            natural += 1
        power += 1


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
