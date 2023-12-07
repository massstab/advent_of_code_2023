#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      06.12.23
   Kurs:      Advent of Code
   Topic:     Wait For It - Part Two
"""

with open("data/day_06.txt") as f:
    lines = f.readlines()

time = int(lines[0][10:].strip().replace(" ", ""))
record = int(lines[1][10:].strip().replace(" ", ""))


def distance_travelled(race_duration, record):
    new_records = 0
    for hold_down_time in range(race_duration):
        time = (race_duration - hold_down_time) * hold_down_time
        if time > record:
            new_records += 1
    return new_records


result = 1
result *= distance_travelled(time, record)
print(result)
