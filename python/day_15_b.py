#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      15.12.23
   Kurs:      Advent of Code
   Topic:     Lens Library
"""

import numpy as np


def get_box_number(hash):
    curr = 0
    for s in hash:
        ASCII = ord(s)
        curr += ASCII
        curr *= 17
        curr %= 256
    return curr


with open("python/data/day_15.txt") as f:
    line = f.readline()

values_list = line.split(',')

labels = []
operations = []

for item in values_list:
    parts = item.split("=")
    box = parts[0] if len(parts) == 2 else parts[0][:-1]
    wert = parts[1] if len(parts) > 1 and parts[1] != "-" else "-"

    labels.append(box)
    operations.append(wert)

box_numbers = []
for h in labels:
    box_numbers.append(get_box_number(h))

boxes_dict = {}
for lab, num, op in zip(labels, box_numbers, operations):
    if op.isnumeric():
        focal = op
        if num in boxes_dict.keys():
            found = False
            for j, l in enumerate(boxes_dict[num]):
                if l[0] == lab:
                    boxes_dict[num][j] = [lab, focal]
                    found = True
            if not found:
                boxes_dict[num].append([lab, focal])
        else:
            boxes_dict[num] = []
            boxes_dict[num].append([lab, focal])
    else:
        if num in boxes_dict.keys():
            for i, lens in enumerate(boxes_dict[num]):
                if lab in lens:
                    del boxes_dict[num][i]

ans = 0
for box in boxes_dict:
    for slot, lenses in enumerate(boxes_dict[box]):
        power = (box + 1) * (slot + 1) * int(lenses[1])
        ans += power
        # print(f"({box + 1}) * {slot+1} * {int(lenses[1])} = {power}")
print(ans)
