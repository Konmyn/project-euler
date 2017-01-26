#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_palindrome(number):
    n = str(number)
    return n ==n[::-1]

def main():
    lychrel = []
    n = 1
    while n<10000:
        counter = 0
        i = n
        while counter<50:
            i = i + int(str(i)[::-1])
            if is_palindrome(i):
                break
            counter += 1
        if counter == 50:
            lychrel.append(n)
        n += 1
    print lychrel
    print "Result: {}".format(len(lychrel))


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
