#!/usr/bin/python
# -*- coding: utf-8 -*-


def divisor_sum(number):
    divisor = 2
    divisors = set([1])
    while divisor <= number**0.5:
        if not number % divisor:
            divisors.add(divisor)
            divisors.add(number / divisor)
        divisor += 1
    return sum(divisors)

def find_amicale(number):
    if divisor_sum(divisor_sum(number)) == number and divisor_sum(number)!= number:
        return True
    else:
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
