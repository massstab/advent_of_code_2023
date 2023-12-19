#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      15.12.23
   Kurs:      Advent of Code
   Topic:     Lavaduct Lagoon
"""

RESET = '\033[0m'


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def get_color_escape(hex_color, background=False):
    rgb = hex_to_rgb(hex_color)
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, *rgb)


def coord_transform(edge):
    max_x = 0
    neg_max_x = 0
    max_y = 0
    neg_max_y = 0
    for i in edge:
        if i[0][0] > max_x:
            max_x += 1
        if i[0][0] < neg_max_x:
            neg_max_x -= 1
        if i[0][1] > max_y:
            max_y += 1
        if i[0][1] < neg_max_y:
            neg_max_y -= 1

    m = max_y + abs(neg_max_y)
    n = max_x + abs(neg_max_x)

    new_edge = []
    for c in edge:
        k = c[0][1] + abs(neg_max_y)
        l = c[0][0] + abs(neg_max_x)
        new_edge.append(((k, l), c[1]))

    return new_edge, (m, n)


with open("python/data/day_18.txt") as f:
    lines = f.readlines()

lines = [line.rsplit() for line in lines]
digplan = []
for line in lines:
    instr = []
    for c in line:
        instr.append(c)
    instr[1] = int(instr[1])
    instr[2] = instr[2][1:-1]
    digplan.append(instr)

edge = [((0, 0), digplan[0][2])]

for instr in digplan:
    hex = instr[2]
    d = instr[0]
    meters = instr[1]
    x, y = edge[-1][0]
    for i in range(1, meters + 1):
        if d == 'U':
            new_y = y - i
            edge.append(((x, new_y), hex))
        elif d == 'R':
            new_x = x + i
            edge.append(((new_x, y), hex))
        elif d == 'D':
            new_y = y + i
            edge.append(((x, new_y), hex))
        elif d == 'L':
            new_x = x - i
            edge.append(((new_x, y), hex))

new_edge, (m, n) = coord_transform(edge)
# print(new_coords)

grid = [['.' for _ in range(n + 1)] for _ in range(m + 1)]
for t in new_edge:
    # char = get_color_escape(f"{t[1]}", False) + \
    #     get_color_escape(f"{t[1]}", False) + '▀' + RESET
    # grid[t[0][0]][t[0][1]] = char
    grid[t[0][0]][t[0][1]] = '#'

counter = 0
visited = []
on_edge = False
inside = False
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i == len(grid) - 1:
            if grid[i][j] == '#':
                continue
        else:
            if grid[i][j] == '.' and grid[i][j+1] == '#':
                counter += 1
                continue
            if grid[i][j] == '#' and grid[i][j+1] == '#':
                on_edge = True
            if grid[i][j] == '#' and grid[i][j+1] == '.':
                on_edge = False
            if 
            
                



        

print(counter)
# for l in grid:
#     print(''.join(l))

#  to high 55854
