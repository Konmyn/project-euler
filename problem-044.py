#!/usr/bin/python
# -*- coding: utf-8 -*-


# # give n, return pn.
# def pentagonal_number(n):
#     return n*(n*3-1)/2

# find the difference of pn and pn+pn-1, 2*pn+pn-1
# def main():
#     n = 2
#     limit = 100
#     while n < limit:
#         suma = pentagonal_number(n-1)+pentagonal_number(n)
#         sumb = pentagonal_number(n-1)+pentagonal_number(n)*2
#         x = n+1
#         while pentagonal_number(x)<=suma:
#             x += 1
#         y = x
#         while pentagonal_number(y)<=sumb:
#             y += 1
#         print n, x-n, y-n
#         n += 1

# # find the growing of pn+1 - pn
# def main():
#     n = 2
#     limit = 100
#     while n<=limit:
#         diff = pentagonal_number(n+1)-pentagonal_number(n)
#         x = 1
#         while pentagonal_number(x)<diff:
#             x += 1
#         print n, x
#         n += 1

# def pentagonal_list(upper_limit):
#     return [x * (3 * x - 1) / 2 for x in xrange(1, upper_limit + 1)]\

# def is_perfect_square(n):
#     return pow(int(pow(n, 0.5)), 2) == n

# def is_pentagonal_number(n):
#     return is_perfect_square(24 * n + 1) and int(pow(24 * n + 1, 0.5)) % 6 == 5

# def main():
#     result = 0
#     n = 1
#     penta_list = list()
#     while not result:
#         penta_next = n * (3 * n - 1) / 2
#         for penta in penta_list:
#             if is_pentagonal_number(penta + penta_next):
#                 if is_pentagonal_number(penta + penta_next * 2):
#                     result = penta
#                     break
#                 elif is_pentagonal_number(penta * 2 + penta_next):
#                     result = penta_next
#                     break
#         else:
#             penta_list.append(penta_next)
#             n += 1
#     print "Result: {}".format(result)

def main():
    # set() is a key data structure, use list would cause 100+ more time cost.
    pent_set = set()
    i = 0
    while True:
        i += 1
        pent = (3*i*i - i)/2
        for p in pent_set:
            if pent-p in pent_set and pent-2*p in pent_set:
                print "Result: {}".format(pent-2*p)
                return
        pent_set.add(pent)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
