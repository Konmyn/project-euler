#!/usr/bin/python
# -*- coding: utf-8 -*-


def generate_diagonal(edge_length):
    round_end = 1
    edge = 1
    step = edge-1
    while edge <= edge_length:
        yield [round_end, round_end-step, round_end-step*2, round_end-step*3]
        edge += 2
        step = edge-1
        round_end += step*4

def main():
    dia = generate_diagonal(1001)
    total_sum = -3 #!!!!!!
    while True:
        try:
            total_sum += sum(dia.next())
        except StopIteration:
            break
    print "Result: {}".format(total_sum)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
