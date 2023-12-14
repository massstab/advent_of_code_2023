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
#print(sum_left)
#print(sum_above)
for j, p in enumerate(patterns):
    (m, n) = p.shape
    for i in range(n):
        print("We are in the L-R for Loop")
        print(f"{i} in  range({n})")
        print("We are in the checking for horizontal symmetry...")

        # horizontal symmetry
        to_check_L = p[:, :i]
        to_check_L_flipped = np.flip(to_check_L, axis=1)
        # print(to_check_L)
        # print(to_check_L_flipped)
        # print("------------")

        if (to_check_L == to_check_L_flipped).all() and ((to_check_L.shape[1]) % 2 == 0) and i > 1:
            print(f"Found LEFT Horizontal Symmetry in pattern {j+1}")
            print(to_check_L)
            print()
            print(to_check_L_flipped)
            print("Adding {} to the sum.".format(to_check_L.shape[1] / 2))
            sum_left += to_check_L.shape[1] / 2

        to_check_R = p[:, i:]
        to_check_R_flipped = np.flip(to_check_R, axis=1)
        print(f"If check: ... and {to_check_R.shape[1]} % 2 == 0 and {i} < {n}-1")
        if (to_check_R == to_check_R_flipped).all() and ((to_check_R.shape[1]) % 2 == 0) and i < n-1:
            print(f"Found RIGHT Horizontal Symmetry in pattern {j+1}")
            print(to_check_R)
            print()
            print(to_check_R_flipped)
            print("Adding {} to the sum.".format(to_check_R.shape[1] / 2 + i))
            sum_left += to_check_R.shape[1] / 2 + i
        print("---------NEXT---------")
    print()
    print("------SYMMETRY CHANGE------")

    for j in range(m):
        print("We are in the U-D for Loop")
        print(f"{j} in  range({m})")
        print("We are in the checking for vertical symmetry...")

        # verrtical symmetry
        to_check_U = p[:j, :]
        to_check_U_flipped = np.flip(to_check_U, axis=0)

        if (to_check_U == to_check_U_flipped).all() and ((to_check_U.shape[0]) % 2 == 0) and j > 1:
            print(f"Found Up Vertical Symmetry in pattern {j+1}")
            print(to_check_U)
            print()
            print(to_check_U_flipped)
            print("Adding {} to the sum".format(100 * to_check_U.shape[0] / 2))
            sum_above += 100 * to_check_U.shape[0] / 2

        to_check_D = p[j:, :]
        to_check_D_flipped = np.flip(to_check_D, axis=0)
        # print("------------")

        if (to_check_D == to_check_D_flipped).all() and ((to_check_D.shape[0]) % 2 == 0) and j < m-1:
            print("fFound Down Vertical Symmetry in pattern {j+1}")
            print(to_check_D)
            print()
            print(to_check_D_flipped)
            print("Adding {} to the sum".format(100 * (to_check_D.shape[0] / 2 + j)))
            sum_above += 100 * (to_check_D.shape[0] / 2 + j)
        print("---------NEXT---------")

ans = sum_left + sum_above

print("Total sum: ", ans)

#  too low: 21136
# not right: 24965
# not right: 25031
# too high: 31268



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
