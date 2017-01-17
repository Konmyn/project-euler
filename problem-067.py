#!/usr/bin/python
# -*- coding: utf-8 -*-


def load_data():
    datas = []
    with open('p067_triangle.txt', 'r') as doc:
        for line in doc:
            datas.append([int(number) for number in line.strip().split()])
    return datas

def main():
    array = load_data()
    triangle_height = len(array)
    max_path = [0]*triangle_height
    max_path[0] = array[0][0]
    for m in range(1, triangle_height):
        i = 0
        copy_list = max_path[:]
        while i < len(array[m]):
            if i == 0:
                max_path[i] = copy_list[i] + array[m][i]
            elif i == len(array[m])-1:
                max_path[i] = copy_list[i-1] + array[m][i]
            else:
                max_path[i] = max(copy_list[i] + array[m][i], copy_list[i-1] + array[m][i])
            i += 1
    print max(max_path)


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
