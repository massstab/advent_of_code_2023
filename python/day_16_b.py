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


def make_seen_dict(m, n):
    seen = {}  # holds all seen tiles (key) with the beam directions [value]

    for i in range(m):
        # initialize a dict for every tile
        for j in range(n):
            seen[(j, i)] = []
    return seen


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

with open("data/day_16.txt") as f:
    lines = f.readlines()

lines = [line.rsplit() for line in lines]
L = []
for line in lines:
    for c in line:
        L.append([*c])

m, n = len(L), len(L[0])

N = []
E = []
S = []
W = []

seen = make_seen_dict(m,n)

for i in seen:
    if i[1] == 0:
        N.append(i)
    if i[0] == n-1:
        E.append(i)
    if i[1] == m-1:
        S.append(i)
    if i[0] == 0:
        W.append(i)

NESW = [N, E, S, W]
maxes = []
global_max = 0
directions = ['v', '<', '^', '>']
for side, d in zip(NESW, directions):
    numbers = []
    for r in side:
        seen = make_seen_dict(m, n)
        step(d, r[0], r[1])
        count = 0
        for i in seen:
            if seen[i] != []:
                count += 1
        numbers.append(count)

    max_value = max(numbers)
    max_index = numbers.index(max_value)
    maxes.append(max_index)
    if max_value > global_max:
        global_max = max_value

print(global_max)

# 14606 is too high
# 14385 is too high
# 7438 correct
