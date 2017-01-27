#!/usr/bin/python
# -*- coding: utf-8 -*-


def cube_length(len_limit = 15):
    n = 1
    length = 1
    len_dict = {}
    len_dict[length] = n
    while length<len_limit:
        n += 1
        if len(str(n**3))>length:
            length = len(str(n**3))
            len_dict[length] = n
    return len_dict

def number_digits(n):
    digit_list = [0]*10
    while n:
        empty_list[n%10] += 1
        n //= 10
    return digit_list

def main():
    cu_len = cube_length()
    len_loop = 1
    while True:
        start = cu_len[len_loop]
        stop = cu_len[len_loop+1]-1
        digit_record_list = []
        number = start
        while number <= stop:
            digit_record_list.append(number_digits(number))
            number += 1
        len_loop += 1
    print "Result: {}".format()


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
