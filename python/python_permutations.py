#!/usr/bin/python
# -*- coding: utf-8 -*-


import itertools


word = 'sample'
my_letters = 'plmeas'

perm = itertools.permutations(my_letters, len(word))

for i in perm:
    if ''.join(i)==word:
        print('Match found!')
        break
else:
    print('No Match!')
