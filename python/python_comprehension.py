#!/usr/bin/python
# -*- coding: utf-8 -*-


lista = range(1, 6)
listb = range(6, 11)
duplist = lista + lista

# list
new_list = [i * i for i in lista if i % 2]

# dict
new_dict = {i: j for i, j in zip(lista, listb)}

# set
new_set = {i for i in duplist}

# generator
gen = (i for i in lista)

print(lista, listb, duplist, new_list, new_dict, new_set, gen)
