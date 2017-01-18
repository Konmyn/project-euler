#!/usr/bin/python
# -*- coding: utf-8 -*-


def decimal_str(denominator):
    dec_str = '0.'
    nominator = 10
    while True:
        dec_str += str(nominator//denominator)
        nominator = nominator%denominator*10
        if nominator == 0 or len(dec_str) > 50:
            break
    return dec_str

def recurring_cycle(denominator):
    nomi_list = [10]
    nominator = 10
    while True:
        nominator = nominator%denominator*10
        if nominator == 0:
            return 0
        elif nominator in nomi_list:
            return len(nomi_list[nomi_list.index(nominator):])
        nomi_list.append(nominator)

def main():
    max_len = 0
    natural = 1
    while natural < 1000:
        if recurring_cycle(natural) > max_len:
            max_len = recurring_cycle(natural)
            d = natural
        natural += 1
    print "Result: {}, Length: {}".format(d, max_len)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
