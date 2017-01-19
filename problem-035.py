#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_prime(n):
    """Returns True if n is prime."""
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

def rotate_list(number):
    length = len(str(number)) - 1
    num_list = []
    for i in range(length):
        number = number%10*10**(length)+number//10
        num_list.append(number)
    return num_list


def main():
    uplimit = 10**6
    natural = 11
    rotate_prime = set([2, 3, 5, 7])
    while natural<uplimit:
        if is_prime(natural) and natural not in rotate_prime:
            n_list = rotate_list(natural)
            flag = True
            for n in n_list:
                if not is_prime(n):
                    flag = False
                    break
            if flag:
                rotate_prime.add(natural)
                for n in n_list:
                    rotate_prime.add(n)
        natural += 2
    print rotate_prime
    print "Result: {}".format(len(rotate_prime))


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
