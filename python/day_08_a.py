#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.23
   Kurs:      Advent of Code
   Topic:     Haunted Wasteland
"""

import numpy as np


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
position = 'AAA'
while not position == 'ZZZ':
    for instr in instructions:
        if position == 'ZZZ':
            break
        elif instr == 'R':
            position = node_dict[position][1]
            steps += 1
        else:
            position = node_dict[position][0]
            steps += 1
print(steps)


# too low 10507
# too low 10508
# too low 10509
# correct 22357

