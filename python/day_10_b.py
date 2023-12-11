#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      10.12.23
   Kurs:      Advent of Code
   Topic:     Pipe Maze
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def is_inside(edges, point):
    (xp, yp) = point
    cnt = 0

    for edge in edges:
        (x1,y1), (x2, y2) = edge
        if (yp < y1) != (x2, y2) and xp < x1 + ((yp - y1)/(y2-y1)) * (x2 -x1):
            cnt += 1
    return cnt%2 == 1

def visualize_graph(graph, grid_size, symbols, start_node):
    # Extract grid dimensions
    m, n = grid_size

    # Create an mxn grid layout starting from the top-left corner
    grid_layout = {(i % m, -(i // m)): i for i in range(len(graph))}

    # Add positions to the graph
    pos = {node: (x, y) for (x, y), node in grid_layout.items()}

    labels = {node: symbols[node] for node in graph.nodes}

    node_color = ['red' if node ==
                  start_node else 'skyblue' for node in graph.nodes]

    cycle_path = nx.find_cycle(graph)

    edge_color = ['darkgreen' if (u, v) in cycle_path or (
        v, u) in cycle_path else 'lightgray' for u, v in graph.edges]

    fig, ax = plt.subplots()
    fig.set_facecolor('black')
    ax.set_facecolor('black')
    # Draw the graph using the grid layout
    nx.draw(graph, pos=pos, with_labels=True, labels=labels, font_weight='bold', node_size=10,
            node_color=node_color, font_color='black', font_size=5, edge_color=edge_color)

    # Show the plot
    plt.show()


flatten = []
with open("python/data/day_10.txt") as f:
    lines = f.readlines()
    for line in lines:
        for c in line.rstrip():
            flatten.append(c)

m = len(line.rstrip())
n = len(lines)
gridsize = (m, n)

len_flatten = len(flatten)


G = nx.Graph()


for i, s in enumerate(flatten):
    if s == "|":
        conn = "NS"
    elif s == "-":
        conn = "EW"
    elif s == "L":
        conn = "NE"
    elif s == "J":
        conn = "NW"
    elif s == "7":
        conn = "SW"
    elif s == "F":
        conn = "SE"
    elif s == ".":
        conn = ""
    elif s == "S":
        conn = "START"
    G.add_node(i, connection=conn)


for node, data in G.nodes(data=True):
    N = node - m
    E = node + 1
    S = node + m
    W = node - 1
    if data["connection"] != '' and data["connection"] != 'START':
        for d in data["connection"]:
            if d == 'N' and 0 < N < len_flatten:
                if 'S' in G.nodes[N]["connection"]:
                    G.add_edge(node, N)
            if d == 'E' and 0 < E < len_flatten:
                if 'W' in G.nodes[E]["connection"] and (node % m == (E % m) - 1):
                    G.add_edge(node, E)
            if d == 'S' and 0 < S < len_flatten:
                if 'N' in G.nodes[S]["connection"]:
                    G.add_edge(node, S)
            if d == 'W' and 0 < W < len_flatten:
                if 'E' in G.nodes[W]["connection"] and (node % m == (W % m) - 1):
                    G.add_edge(node, W)
    if data["connection"] == "START":
        start_node_index = node
        if 'S' in G.nodes[N]["connection"]:
            G.add_edge(node, N)
        if 'W' in G.nodes[E]["connection"]:
            G.add_edge(node, E)
        if 'N' in G.nodes[S]["connection"]:
            G.add_edge(node, S)
        if 'E' in G.nodes[W]["connection"]:
            G.add_edge(node, W)

    # print("####")


M = np.reshape(G, (-1, m))
P = np.reshape(flatten, (-1, m))
points_idx = []
# print(P)
P = list(zip(*np.where(P == '.')))
edges = cycle_path = nx.find_cycle(G)
edges_new = []
for edge in edges:
    x1, y1 = np.where(M == edge[0])
    x2, y2 = np.where(M == edge[1])
    new = (x1, y1), (x2, y2)
    edges_new.append(new)
    print(new)

print(M, edges)


for i, edge in enumerate(edges_new):  
    print(is_inside(edge, P[i]))


# visualize_graph(G, gridsize, symbols=dict(
#     enumerate(flatten)), start_node=start_node_index)
