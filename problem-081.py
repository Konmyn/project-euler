#!/usr/bin/python
# -*- coding: utf-8 -*-


LIST_XY = []

def load_data():
    datas = []
    with open('p081_matrix.txt') as doc:
        for line in doc:
            datas.append([int(number) for number in line.strip().split(',')])
    return datas

# easy to understand but hard for computer to compute.
# did not get answer from this method, need more check.
def find_min_path(list_xy, x, y):
    if x==0 and y==0:
        return list_xy[x][y]
    elif x==0:
        return find_min_path(list_xy, x, y-1)+list_xy[x][y]
    elif y==0:
        return find_min_path(list_xy, x-1 ,y)+list_xy[x][y]
    else:
        return min(find_min_path(list_xy, x-1 ,y), find_min_path(list_xy, x, y-1))+list_xy[x][y]

# easy fast way
def direct_method(list_xy):
    cache = list_xy[:]
    for i in range(1, 80):
        cache[0][i] += cache[0][i-1]
        cache[i][0] += cache[i-1][0]
    for y in range(1, 80):
        for x in range(1, 80):
            cache[x][y] += min(cache[x][y-1], cache[x-1][y])
    return cache[79][79]

def main():
    LIST_XY =load_data()
    # target = find_min_path(LIST_XY, 79. 79)
    target = direct_method(LIST_XY)
    print "Result: {}".format(target)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
