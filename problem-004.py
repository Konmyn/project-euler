#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime
from tools.common import is_palindromic


@runTime
def brute_force_method(digits=3):
    result = [0, 0, 0] #[m, n, m*n]
    # both m,n should be odd since the result is starting with 9.
    for n in xrange(10**digits-1, 10**(digits-1)-1, -2):
        for m in xrange(10**digits-1, n-1, -2):
            if result[2] >= m*n:
                break
            elif is_palindromic(m*n):
                result = [m, n, m*n]
                break
    print "Result: {} * {} = {}".format(*result)

# this method only support 3 digits number with their product is 5 digits number.
# abccba = 100001*a + 10010*b + 1100*c = "11"*(9091*a + 910*b + 11*c)
@runTime
def by_finding_pattern(digits=3):
    result = [0, 0, 0] #[m, n, m*n]
    # both m,n should be odd since the result is starting with 9.
    for n in xrange(10**digits-1, 10**(digits-1)-1, -2):
        m_head = n//11 if (n//11)%2 else (n//11)-1
        # 979=11*90 is the smallest odd number that has factor 11.
        for m in xrange(11*m_head if n%11 else 10**digits-1,
                         n-1, -11 if n%11 else -2):
            if result[2] >= m*n:
                break
            elif is_palindromic(m*n):
                result = [m, n, m*n]
                break
    print "Result: {} * {} = {}".format(*result)


if __name__ == "__main__":
    brute_force_method()
    by_finding_pattern()