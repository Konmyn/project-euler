#!/usr/bin/python
# -*- coding: utf-8 -*-


FLAG = 0

def find_amicale(number):
    global FLAG
    divisor = 2
    divisors = set([1])
    while divisor <= number**0.5:
        if not number % divisor:
            divisors.add(divisor)
            divisors.add(number / divisor)
        divisor += 1
    ami = sum(divisors)
    if FLAG:
        if ami == FLAG:
            return True
        else:
            return False
    else:
        FLAG = number
    if find_amicale(ami):
        FLAG = 0
        return True
    else:
        FLAG = 0
        return False

def main():
    amicable = set()
    natural = 2
    while natural < 10000:
        if find_amicale(natural):
            amicable.add(natural)
        natural += 1
    print amicable
    print "Result: {}".format(sum(amicable))


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
