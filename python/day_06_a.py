#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      06.12.23
   Kurs:      Advent of Code
   Topic:     Wait For It - Part One
"""

import numpy as np

with open("data/day_06.txt") as f:
    lines = f.readlines()

times = np.array(lines[0][10:].split()).astype(np.int32)
records = np.array(lines[1][10:].split()).astype(np.int32)

def distance_travelled(race_duration, record):
    new_records = 0
    for hold_down_time in range(race_duration):
        time = (race_duration - hold_down_time) * hold_down_time
        if time > record:
            new_records += 1
    return new_records

result = 1
for i in range(len(times)):
    result *= distance_travelled(times[i], records[i])
print(result)


# 22550 too low