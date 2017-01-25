#!/usr/bin/python
# -*- coding: utf-8 -*-


PRIME_LIST = []

def gen_prime_list(start=1000, stop=9999):
    number = start
    while number<=stop:
        if is_prime(number):
            PRIME_LIST.append(number)
        number += 1
    return

def is_prime(n):
    """Returns True if n is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
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

def is_permutation(x, y, z):
    a = [0]*10
    b = [0]*10
    c = [0]*10
    while x:
        a[x%10] += 1
        x //= 10
    while y:
        b[y%10] += 1
        y //= 10
    while z:
        c[z%10] += 1
        z //= 10
    if a == b == c:
        return True
    else:
        return False

def main():
    gen_prime_list()
    i = len(PRIME_LIST)-1
    while i>1:
        j = i-1
        while j>0:
            diff = PRIME_LIST[j]*2-PRIME_LIST[i]
            if diff in PRIME_LIST[:j]:
                if is_permutation(diff, PRIME_LIST[j], PRIME_LIST[i]):
                    target = [diff, PRIME_LIST[j], PRIME_LIST[i]]
                    if 1487 not in target:
                        candidates = ''
                        for num in target:
                            candidates += str(num)
                        print "Result: {}".format(candidates)
                        return
            j -= 1
        i -= 1


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
