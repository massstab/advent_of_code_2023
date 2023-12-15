#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      15.12.23
   Kurs:      Advent of Code
   Topic:     Lens Library
"""

import sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)

with open("data/day_14.txt") as f:
    line = f.readline()

values_list = line.split(',')
print(values_list)



init = []
for v in values_list:
    curr = 0
    for s in v:
        print("s: ",s)
        ASCII = ord(s)
        print("curr: ", curr)
        curr += ASCII
        print("curr: ", curr)
        curr *= 17
        print("curr: ", curr)
        curr %= 256
        print("curr: ", curr)
        print("----NEXT----")
    init.append(curr)

print(sum(init))
