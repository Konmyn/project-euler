#!/usr/bin/python
# -*- coding: utf-8 -*-


import collections


datatypes = set([
    int,
    float,
    str,
    set,
    dict,
    tuple,
    list,
])

for datatype in datatypes:
    if isinstance(datatype(), collections.Hashable):
        print('{} type is hashable'.format(datatype.__name__))
    else:
        print('{} type *not* is hashable'.format(datatype.__name__))
