#!/usr/bin/python
# -*- coding: utf-8 -*-

# I do not like this problem because the description is bad, very very bad!

# I use this simplified function because I know
# the number I check is greater than 100000.
def is_prime(n):
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    # a prime (except 2 and 3) is of form 6k - 1 or 6k + 1
    while i * i <= n:
        if not n % i or not n % (i + 2):
            return False
        i += 6
    return True

def is_8_prime_family(num, digit):
    counter = 0
    for i in '0123456789':
        new_num = int(num.replace(digit, i))
        if new_num>100000 and is_prime(new_num):
            counter += 1
    if counter == 8:
        return True
    return False

def main():
    number = 100001
    while number < 1000000:
        if is_prime(number):
            str_num = str(number)
            if str_num.count('0') and is_8_prime_family(str_num, '0') or \
               str_num.count('1') and str_num[-1] != '1' and is_8_prime_family(str_num, '1') or \
               str_num.count('2') and is_8_prime_family(str_num, '2'):
                break
        number += 2
    print "Result: {}".format(number)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
