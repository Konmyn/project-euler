#!/usr/bin/python
# -*- coding: utf-8 -*-


def pentagonal_list(upper_limit):
    return [x * (3 * x - 1) / 2 for x in xrange(1, upper_limit + 1)]


def is_perfect_square(n):
    return pow(int(pow(n, 0.5)), 2) == n


def is_pentagonal_number(n):
    return is_perfect_square(24 * n + 1) and int(pow(24 * n + 1, 0.5)) % 6 == 5

def main():
    upper_limit = 3000
    pen_list = pentagonal_list(upper_limit)
    result_list = []
    j = 2
    while j < upper_limit:
        i = 0
        while i < upper_limit - j:
            if not (pen_list[i] + pen_list[i + j]) % 2 and not (pen_list[i + j] - pen_list[i]) % 2:
                if is_pentagonal_number((pen_list[i] + pen_list[i + j]) / 2) and is_pentagonal_number((pen_list[i + j] - pen_list[i]) / 2):
                    result_list.append([pen_list[i], pen_list[i + j]])
            i += 1
        j += 1
    print "Result: {} -> {}".format(upper_limit, result_list)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)

# Result: 6000 -> []
# Time used(s): 300.045874119

╭─ethan@EthanMAC.local ~/workspace/project/project-euler  ‹master*›
╰─➤  python problem-044.py
Result: 2000 -> []
Time used(s): 1.4548060894
╭─ethan@EthanMAC.local ~/workspace/project/project-euler  ‹master*›
╰─➤  python problem-044.py
Result: 4000 -> [[5482660, 8602840]]
Time used(s): 6.20153999329
╭─ethan@EthanMAC.local ~/workspace/project/project-euler  ‹master*›
╰─➤  python problem-044.py
Result: 6000 -> [[5482660, 8602840]]
Time used(s): 13.0637319088
╭─ethan@EthanMAC.local ~/workspace/project/project-euler  ‹master*›
╰─➤  python problem-044.py
Result: 3000 -> [[5482660, 8602840]]
Time used(s): 3.24665093422
