#!/usr/bin/python
# -*- coding: utf-8 -*-


from tools.runningTime import runTime


@runTime
def recurrence_method(uplimit=4*10**6):
    # starting with 0 or 1 do not make difference to the result.
    a, b = 1, 1
    target_list = []
    while b <= uplimit:
        if b%2==0:
            target_list.append(b)
        a, b = b, a+b
    print "Result: {}".format(sum(target_list))

# kind of magic, by others research.
# http://blog.dreamshire.com/project-euler-2-solution/
# based on f(n)=f(n-1)+f(n-2), try to find f(3n) = g(f(3(n-1)), f(3(n-2)))
@runTime
def by_formula(uplimit=4*10**6):
    a, b = 0, 2
    while b <= uplimit:
        a, b = b, 4*b+a
    print "Result: {}".format((a+b-2)//4)


if __name__ == "__main__":
    # these 2 function speed is not that different.
    recurrence_method()
    by_formula()
