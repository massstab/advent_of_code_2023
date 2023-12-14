#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      13.12.23
   Kurs:      Advent of Code
   Topic:     Point of Incidence
"""

import sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)

with open("python/data/day_13.txt") as f:
    lines = f.readlines()

patterns = []
pattern = []
for i, line in enumerate(lines):
    if i == len(lines) - 1:
        pattern.append(line.rstrip())
    if line.strip() != '' and i != len(lines) - 1:
        pattern.append(line.rstrip())
    else:
        array_2d = np.array([list(row) for row in pattern])
        patterns.append(array_2d)
        pattern = []

# print(patterns)
sum_left = 0
sum_above = 0
print(sum_left)
print(sum_above)
for j, p in enumerate(patterns):
    (m, n) = p.shape
    for i in range(2, n, 2):
        # horizontal symmetry
        to_check_L = p[:, :i]
        to_check_L_flipped = np.flip(to_check_L, axis=1)
        # print(to_check_L)
        # print(to_check_L_flipped)
        # print("------------")

        if (to_check_L == to_check_L_flipped).all():
            sum_left += to_check_L.shape[1] / 2

        to_check_R = p[:, i:]
        to_check_R_flipped = np.flip(to_check_R, axis=1)
        # print(to_check_R)
        # print(to_check_R_flipped)
        # print("------------")
        if (to_check_R == to_check_R_flipped).all():
            sum_left += to_check_R.shape[1] / 2 + i

        # verrtical symmetry
        to_check_U = p[:i, :]
        to_check_U_flipped = np.flip(to_check_U, axis=0)

        if (to_check_U == to_check_U_flipped).all():
            sum_above += to_check_U.shape[0] / 2

        to_check_D = p[-i:, :]
        to_check_D_flipped = np.flip(to_check_D, axis=0)
        print(to_check_D)
        print(to_check_D_flipped)
        print("------------")

        if (to_check_D == to_check_D_flipped).all():
            sum_above += 100 * (to_check_D.shape[0] / 2 + i)

ans = sum_left + sum_above

print(ans)

#  too low: 21136



# ans:  0
# Horizontal:  0
# ans:  300
# vertical:  1
# ans:  301
# vertical:  2
# ans:  307
# Horizontal:  3
# ans:  1507
# Horizontal:  4
# ans:  1907
# Horizontal:  5
# ans:  2207
# vertical:  6
# ans:  2208
# vertical:  7
# ans:  2220
# Horizontal:  8


# import sys
# import re
# from copy import deepcopy
# from math import gcd
# from collections import defaultdict, Counter, deque
# D = open("python/data/day_13.txt").read().strip()
# L = D.split('\n')
# G = [[c for c in row] for row in L]

# for part2 in [False, True]:
#     ans = 0
#     for i, grid in enumerate(D.split('\n\n')):
#         if not part2:
#             print("ans: ", ans)
#         G = [[c for c in row] for row in grid.split('\n')]
#         R = len(G)
#         C = len(G[0])
#         # vertical symmetry
#         for c in range(C-1):
#             badness = 0
#             for dc in range(C):
#                 left = c-dc
#                 right = c+1+dc
#                 if 0 <= left < right < C:
#                     for r in range(R):
#                         if G[r][left] != G[r][right]:
#                             badness += 1
#             if badness == (1 if part2 else 0):
#                 if not part2:
#                     print("vertical: ", i)
#                 ans += c+1
#         for r in range(R-1):
#             badness = 0
#             for dr in range(R):
#                 up = r-dr
#                 down = r+1+dr
#                 if 0 <= up < down < R:
#                     for c in range(C):
#                         if G[up][c] != G[down][c]:
#                             badness += 1
#             if badness == (1 if part2 else 0):
#                 if not part2:
#                     print("Horizontal: ", i)
#                 ans += 100*(r+1)
#     # print(ans)
