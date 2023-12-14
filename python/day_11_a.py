#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      10.12.23
   Kurs:      Advent of Code
   Topic:     Pipe Maze
   Comment:   Code is amazingly slow!
"""

import numpy as np
import networkx as nx
from helpers import visualize_graph, insert_to_numpy
import matplotlib.pyplot as plt


flatten = []
with open("python/data/day_11.txt") as f:
    lines = f.readlines()
    for line in lines:
        for c in line.rstrip():
            flatten.append(c)
M = np.reshape(flatten, (-1, len(line)))
M = insert_to_numpy(M)
G = nx.grid_2d_graph(*M.shape)

galaxies = list(zip(*np.where(M == '#')))

shortests = []
done = []
for g1 in galaxies:
    print(g1)
    for g2 in galaxies:
        if g1 != g2 and ((g2, g1) not in done):
            path = nx.shortest_path(G, source=g1, target=g2)
            # print(path)
            path_edges = list(zip(path, path[1:]))
            shortests.append(path_edges)
        done.append((g1, g2))

print(len(shortests))
sum = 0
for path in shortests:
    sum += len(path)
    print(len(path))

print(sum)

# visualize_graph(G, M.shape, symbols=dict(zip(G.nodes, M.flatten())), edges=shortests[4])

#  took years but solved 10289334
