#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.23
   Kurs:      Advent of Code
   Topic:     Mirage Maintenance
"""

import numpy as np


histories = []
with open("python/data/day_09.txt") as f:
    lines = f.readlines()
    for line in lines:
        histories.append(line.split())


histories = np.array(histories).astype(np.int32)

sum = 0
for history in histories:
    summands = []
    # print(history)
    history_diff = np.diff(history)
    while history_diff.any():
        summands.append(history_diff[-1])
        # print(history_diff)
        history_diff = np.diff(history_diff)

    # print(history_diff)
    # print(summands)
    res = 0
    for s in np.flip(summands):
        res += s
    sum += res + history[-1]
    # print("#########")
print(sum)
# 