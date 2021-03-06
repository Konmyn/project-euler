#!/usr/bin/python
# -*- coding: utf-8 -*-

# brute force method below:
def find_min_number_have_n_divisors(divisor_count):
    if not isinstance(divisor_count, int):
        raise TypeError
    if 0 <= divisor_count < 2:
        return divisor_count
    elif divisor_count < 0:
        raise ValueError
    target = 2
    while True:
        counter = 1
        start = 2
        stop = int(target**0.5)
        while start <= stop:
            if target % start == 0:
                counter += 1
            start += 1
        if stop**2 == target:
            counter = counter * 2 - 1
        else:
            counter *= 2
        if counter == divisor_count:
            break
        target += 1
    return target

# check how many divisor one number may have:
def how_many_divisors_for_one_number(number):
    if not isinstance(number, int):
        raise TypeError
    if 0 <= number < 2:
        return number
    elif number < 0:
        raise ValueError
    counter = 1
    stop = int(number**0.5)
    start = 2
    while start <= stop:
        if number % start == 0:
            counter += 1
        start += 1
    if stop**2 == number:
        counter = counter * 2 - 1
    else:
        counter *= 2
    return counter

# find primes in order
# +2 和 6K+/-1的方法时间一样啊，见commit历史。
def get_primes_and_positions(limit):
    if not isinstance(limit, int):
        raise TypeError
    if limit < 5:
        raise ValueError
    count = 5
    the_number = 11
    while count <= limit:
        stop = int(the_number**0.5)
        divisor = 3
        is_prime = True
        while divisor <= stop:
            if not the_number % divisor:
                is_prime = False
                break
            divisor += 2
        if is_prime:
            # the nth prime and the prime.
            yield (count, the_number)
            count += 1
        the_number += 2

# 这道题果然比较复杂，通过简单的找规律，找到了一些皮毛，后来发现嵌套不少其他条件，可能需要动态规划解决了，分支比较多。
# the number which have 2**6 divisor is 2*2*6*5*7*9 = 7560
def main():
    result = 7560
    for i, j in get_primes_and_positions(500500-2):
        result = result * j % 500500507
        if not i % 5005:
            print i, j
    print result


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
