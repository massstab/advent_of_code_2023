#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      15.12.23
   Kurs:      Advent of Code
   Topic:     Hot Springs
   Comment:   Totally inspired by Jonathan Paulson. I only wrote check_arrangement by myself
"""


def check_arrangement(arr, rule):
    rule_checkt = []
    len_group = 0  # size of contiguous group of damaged springs
    group_number = 0  # the nth group in the row
    damaged_spring = False  # checks if we are on a damaged spring
    inside_group = False
    for i, char in enumerate(arr):
        if char == '#':
            damaged_spring = True
            inside_group = True
            len_group += 1
        else:
            damaged_spring = False
            inside_group = False
        if not inside_group and len_group > 0:
            group_number += 1
            rule_checkt.append(len_group)
            len_group = 0
        if i == len(arr) - 1 and inside_group:
            rule_checkt.append(len_group)
    return rule_checkt == rule


def find_unknown(arr):
    idxs = []
    for i, j in enumerate(arr):
        if j == '?':
            idxs.append(i)
    return idxs


def permut(arr, rule, i):
    if i == len(arr):
        return 1 if check_arrangement(arr, rule) else 0
    if arr[i] == '?':
        return (permut(arr[:i] + '#' + arr[i+1:], rule, i+1) +
                permut(arr[:i] + '.' + arr[i+1:], rule, i+1))
    else:
        return permut(arr, rule, i+1)


with open("python/data/day_12.txt") as f:
    lines = f.readlines()

splitted = [line.rstrip().split(' ') for line in lines]
splitted = [[v[0], v[1].split(',')] for v in splitted]

for i in range(len(splitted)):
    for j in range(len(splitted[i][1])):
        splitted[i][1][j] = int(splitted[i][1][j])

arrs = []
rules = []
for i in splitted:
    arrs.append(i[0])
    rules.append(i[1])

sum = 0
for arr, rule in zip(arrs, rules):
    score = permut(arr, rule, 0)
    sum += score
print(sum)
