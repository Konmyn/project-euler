#!/usr/bin/python
# -*- coding: utf-8 -*-


def generate_triangle(n=1, stop=None):
    if stop is None:
        stop = n+1
    while True:
        yield n*(n+1)/2
        n += 1
        if n == stop:
            break
    return

def generate_pentagonal(n=1, stop=None):
    if stop is None:
        stop = n+1
    while True:
        yield n*(3*n-1)/2
        n += 1
        if n == stop:
            break
    return

def generate_hexagonal(n=1, stop=None):
    if stop is None:
        stop = n+1
    while True:
        yield n*(2*n-1)
        n += 1
        if n == stop:
            break
    return

def main():
    # T285 = P165 = H143 = 40755
    n_tri = 286
    while True:
        x = generate_triangle(n_tri).next()
        y = generate_pentagonal(166, n_tri)
        while True:
            cachey = y.next()
            if cachey == x:
                z = generate_hexagonal(144, n_tri)
                while True:
                    cachez = z.next()
                    if cachez == x:
                        print "Result: {}".format(x)
                        return
                    elif cachez>x:
                        break
            elif cachey>x:
                break
        n_tri += 1
        if n_tri%100==0:
            print n_tri


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
