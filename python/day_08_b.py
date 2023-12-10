#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.23
   Kurs:      Advent of Code
   Topic:     Haunted Wasteland
   Credits:   Larv Jurv on Reddit for lcm idea
"""

import numpy as np
from math import lcm


with open("python/data/day_08.txt") as f:
    lines = f.readlines()
    instructions = lines[0].rstrip()
    nodes = []
    for line in lines[2:]:
        nodes.append(line.split())
node_dict = {}
for node in nodes:
    node_dict[node[0]] = (node[2][1:4], node[3][:3])

steps = 0
positions = []

for s in node_dict:
    if s[2] == 'A':
        positions.append(s)


numbers = []
for i, p in enumerate(positions):
    count = 0
    while positions[i][2] != 'Z':
        instr = instructions[count%len(instructions)]
        if instr == 'R':
            positions[i] = node_dict[positions[i]][1]
        else:
            positions[i] = node_dict[positions[i]][0]
        count += 1
    numbers.append(count)

print(lcm(*numbers))    
