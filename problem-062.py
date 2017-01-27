#!/usr/bin/python
# -*- coding: utf-8 -*-


def cube_length(len_limit = 20):
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
        digit_list[n%10] += 1
        n //= 10
    return digit_list

def main():
    cu_len = cube_length()
    len_loop = 1
    target = None
    while True:
        start = cu_len[len_loop]
        stop = cu_len[len_loop+1]-1
        digit_record_list = []
        number = start
        while number <= stop:
            digit_record_list.append(number_digits(number**3))
            number += 1
        list_len = stop - start + 1
        per_number_list = [0]*list_len
        i = 0
        while i < list_len:
            cache_list = [i+start]
            j = i + 1
            while j < list_len:
                if digit_record_list[i] == digit_record_list[j]:
                    cache_list.append(j+start)
                j += 1
            per_number_list[i] = cache_list
            i += 1
        for ele in per_number_list:
            if len(ele) == 5:
                target = ele
                break
        if target:
            break
        len_loop += 1
    print "Result: {}".format(target[0]**3)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
