#!/usr/bin/python
# -*- coding: utf-8 -*-


TRIANGLE_NUM_LIST = [10, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

def load_data():
    with open('p042_words.txt') as doc:
        datas = doc.read().strip('"').split('","')
    return datas

def is_triangle_number(number):
    if number in TRIANGLE_NUM_LIST[1:]:
        return True
    elif number<TRIANGLE_NUM_LIST[-1]:
        return False
    else:
        flag = TRIANGLE_NUM_LIST[0] + 1
        tri_num = flag*(flag+1)//2
        while tri_num<number:
            TRIANGLE_NUM_LIST.append(tri_num)
            flag += 1
            tri_num = flag*(flag+1)//2
        TRIANGLE_NUM_LIST.append(tri_num)
        TRIANGLE_NUM_LIST[0] = flag
        if tri_num == number:
            return True
        else:
            return False

def is_triangle_word(word):
    word_sum = 0
    for character in word:
        word_sum += ord(character) - 64
    if is_triangle_number(word_sum):
        return True
    else:
        return False

def main():
    words = load_data()
    counter = 0
    for word in words:
        if is_triangle_word(word):
            counter += 1
    print TRIANGLE_NUM_LIST
    print "Result: {}".format(counter)

if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
