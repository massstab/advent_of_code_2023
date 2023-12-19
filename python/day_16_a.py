#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      16.12.23
   Kurs:      Advent of Code
   Topic:     The Floor Will Be Lava
"""

from collections import defaultdict, Counter, deque
from math import gcd
from copy import deepcopy
import re
import sys
sys.setrecursionlimit(10000)

with open("data/day_16.txt") as f:
    lines = f.readlines()

lines = [line.rsplit() for line in lines]
L = []
for line in lines:
    for c in line:
        L.append([*c])

m, n = len(L), len(L[0])

seen = {}  # holds all seen tiles (key) with the beam directions [value]

for i in range(m):
    # initialize a key/value pair for every tile
    for j in range(n):
        seen[(j, i)] = []

def step(aim, x, y):
    symbols = ['.', '^', '>', 'v', '<']
    if y < 0 or y > m-1 or x < 0 or x > n-1:
        return 0
    elif aim in seen[(x, y)]:
        return 1

    seen[(x, y)].append(aim)
    if aim == '^':
        if 0 < y < m:
            if L[y-1][x] in symbols:
                step(aim, x, y-1)
            elif L[y-1][x] == '/':
                step('>', x, y-1)
            elif L[y-1][x] == '\\':
                step('<', x, y-1)
            elif L[y-1][x] == '|':
                step(aim, x, y-1)
            elif L[y-1][x] == '-':
                step('>', x, y-1)
                step('<', x, y-1)
                
    if aim == '>':
        if 0 <= x < n-1:
            if L[y][x+1] in symbols:
                step(aim, x+1, y)
            elif L[y][x+1] == '/':
                step('^', x+1, y)
            elif L[y][x+1] == '\\':
                step('v', x+1, y)
            elif L[y][x+1] == '|':
                step('^', x+1, y)
                step('v', x+1, y)
            elif L[y][x+1] == '-':
                step(aim, x+1, y)
    if aim == 'v':
        if 0 <= y < m-1:
            if L[y+1][x] in symbols:
                step(aim, x, y+1)
            elif L[y+1][x] == '/':
                step('<', x, y+1)
            elif L[y+1][x] == '\\':
                step('>', x, y+1)
            elif L[y+1][x] == '|':
                step(aim, x, y+1)
            elif L[y+1][x] == '-':
                step('>', x, y+1)
                step('<', x, y+1)
    if aim == '<':
        if 0 < x < n:
            if L[y][x-1] in symbols:
                step(aim, x-1, y)
            elif L[y][x-1] == '/':
                step('v', x-1, y)
            elif L[y][x-1] == '\\':
                step('^', x-1, y)
            elif L[y][x-1] == '|':
                step('^', x-1, y)
                step('v', x-1, y)
            elif L[y][x-1] == '-':
                step(aim, x-1, y)

    return


step('v', 0, 0)

count = 0
for i in seen:
    if seen[i] != []:
        L[i[1]][i[0]] = '#'
        count += 1

#for line in L:
#    print(''.join(line))

print(count)

#  too low: 218
#  too high: 9835
#  not: 7185
#  too low: 44
#  correct: 7199
