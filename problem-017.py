#!/usr/bin/python
# -*- coding: utf-8 -*-

number_dict = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
}

def one_or_two_digits(number):
    if number < 20:
        return number_dict[number]
    else:
        if number % 10:
            return '{}-{}'.format(number_dict[number//10*10],number_dict[number%10])
        else:
            return number_dict[number]

def three_digits(number):
    if number%100:
        return '{} {} and {}'.format(number_dict[number//100],number_dict[100],one_or_two_digits(number%100))
    else:
        return '{} {}'.format(number_dict[number//100],number_dict[100])

def four_digits(number):
    if number%1000:
        if number//100%10:
            return '{} {}, {}'.format(number_dict[number//1000],number_dict[1000],three_digits(number%1000))
        else:
            return '{} {} and {}'.format(number_dict[number//1000],number_dict[1000],one_or_two_digits(number%1000))
    else:
        return '{} {}'.format(number_dict[number//1000],number_dict[1000])

def number_to_words(number):
    digits = len(str(number))
    if digits < 3:
        return one_or_two_digits(number)
    elif digits == 3:
        return three_digits(number)
    elif digits == 4:
        return four_digits(number)
    else:
        return


def main():
    counter = 0
    for natural in range(1,1001):
        text = number_to_words(natural)
        counter += len(text)-text.count(' ')-text.count('-')
    print "Result: {}".format(counter)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
