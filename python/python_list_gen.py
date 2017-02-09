#!/usr/bin/python
# -*- coding: utf-8 -*-


r = range(10)
s = range(20)

# below both work for generate list
m = [a*b for a in r for b in r]
n = [a+b for a in r for b in s]
