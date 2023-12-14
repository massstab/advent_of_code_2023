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

print_on = False
sum_left = 0
sum_above = 0
for k, p in enumerate(patterns):
    (m, n) = p.shape
    for i in range(n):
        if print_on:
            print("We are in the L-R for Loop")
            print(f"{i} in  range({n})")
            print("We are in the checking for vertical symmetry...")

        ############################
        # vertical symmetry LEFT #
        ############################

        to_check_L = p[:, :i]
        to_check_L_flipped = np.flip(to_check_L, axis=1)
        idxs = [index for index in zip(*np.where(to_check_L != to_check_L_flipped))]
        smudged = False
        if len(idxs) == 2 and ((to_check_L.shape[1]) % 2 == 0) and i > 1:
            smudged = True
            smudged_idx = idxs[0]
            if print_on:
                print("It's SMUDGED!")
                print(f"Smudged idx: {smudged_idx}")
                print()
                print("Before cleaning: ")
                print(to_check_L)
            to_check_L[smudged_idx] = '.' if to_check_L[smudged_idx] == '#' else '#'
            to_check_L_flipped = np.flip(to_check_L, axis=1)
            if print_on:
                print("After cleaning: ")
                print(to_check_L_flipped)

        if (to_check_L == to_check_L_flipped).all() and ((to_check_L.shape[1]) % 2 == 0) and i > 1 and smudged:
            if print_on:
                print(f"Found LEFT vertical Symmetry in pattern {k+1}")
                print("Adding {} to the sum.".format(to_check_L.shape[1] / 2))
            sum_left += to_check_L.shape[1] / 2
            to_check_L[smudged_idx] = '.' if to_check_L[smudged_idx] == '#' else '#'


        #############################
        # vertical symmetry Right #
        ############################3

        to_check_R = p[:, i:]
        to_check_R_flipped = np.flip(to_check_R, axis=1)
        idxs = [index for index in zip(*np.where(to_check_R != to_check_R_flipped))]
        smudged = False
        if len(idxs) == 2 and ((to_check_R.shape[1]) % 2 == 0) and i < n-1:
            smudged = True
            smudged_idx = idxs[0]
            if print_on:
                print("It's SMUDGED!")
                print(f"Smudged idx: {smudged_idx}")
                print()
                print("Before cleaning: ")
                print(to_check_R)
            to_check_R[smudged_idx] = '.' if to_check_R[smudged_idx] == '#' else '#'  
            to_check_R_flipped = np.flip(to_check_R, axis=1)
            if print_on:
                print("After cleaning: ")
                print(to_check_R_flipped)

        if (to_check_R == to_check_R_flipped).all() and ((to_check_R.shape[1]) % 2 == 0) and i < n-1 and smudged:
            if print_on:
                print(f"Found RIGHT vertical Symmetry in pattern {k+1}")
                print("Adding {} to the sum.".format(to_check_R.shape[1] / 2 + i))
            sum_left += to_check_R.shape[1] / 2 + i
            to_check_R[smudged_idx] = '.' if to_check_R[smudged_idx] == '#' else '#'  

        print("---------NEXT---------") if print_on else None
    print() if print_on else None
    print("------SYMMETRY CHANGE------") if print_on else None

    for j in range(m):
        if print_on:
            print("We are in the U-D for Loop")
            print(f"{j} in  range({m})")
            print("We are in the checking for horizontal symmetry...")

        ##########################
        # horizontal symmetry UP #
        ##########################

        to_check_U = p[:j, :]
        to_check_U_flipped = np.flip(to_check_U, axis=0)
        idxs = [index for index in zip(*np.where(to_check_U != to_check_U_flipped))]
        smudged = False
        if len(idxs) == 2 and ((to_check_U.shape[0]) % 2 == 0) and j > 1:
            smudged = True
            smudged_idx = idxs[0]
            if print_on:
                print("It's SMUDGED!")
                print(f"Smudged idx: {smudged_idx}")
                print()
                print("Before cleaning: ")
                print(to_check_U)
            to_check_U[smudged_idx] = '.' if to_check_U[smudged_idx] == '#' else '#'
            to_check_U_flipped = np.flip(to_check_U, axis=0)
            if print_on:
                print("After cleaning: ")
                print(to_check_U_flipped)
        if (to_check_U == to_check_U_flipped).all() and ((to_check_U.shape[0]) % 2 == 0) and j > 1 and smudged:
            if print_on:
                print("Found Up horizontal Symmetry in pattern {}".format(k+1))
                print("Adding {} to the sum".format(100 * to_check_U.shape[0] / 2))
            sum_above += 100 * to_check_U.shape[0] / 2
            to_check_U[smudged_idx] = '.' if to_check_U[smudged_idx] == '#' else '#'


        ############################
        # horizontal symmetry DOWN #
        ############################

        to_check_D = p[j:, :]
        to_check_D_flipped = np.flip(to_check_D, axis=0)
        idxs = [index for index in zip(*np.where(to_check_D != to_check_D_flipped))]
        smudged = False
        if len(idxs) == 2 and ((to_check_D.shape[0]) % 2 == 0) and j < m-1:
            smudged = True
            smudged_idx = idxs[0]
            if print_on:
                print("It's SMUDGED!")
                print(f"Smudged idx: {smudged_idx}")
                print()
                print("Before cleaning: ")
                print(to_check_D)
            to_check_D[smudged_idx] = '.' if to_check_D[smudged_idx] == '#' else '#'
            to_check_D_flipped = np.flip(to_check_D, axis=0)
            if print_on:
                print("After cleaning: ")
                print(to_check_D_flipped)

        if (to_check_D == to_check_D_flipped).all() and ((to_check_D.shape[0]) % 2 == 0) and j < m-1 and smudged:
            if print_on:
                print("Found Down horizontal Symmetry in pattern {}".format(k+1))
                print("Adding {} to the sum".format(100 * (to_check_D.shape[0] / 2 + j)))
            sum_above += 100 * (to_check_D.shape[0] / 2 + j)
            to_check_D[smudged_idx] = '.' if to_check_D[smudged_idx] == '#' else '#'

        print("---------NEXT---------") if print_on else None

ans = int(sum_left + sum_above)

print("Total sum: ", ans)

#  too high: 41170
# correct: 39359
