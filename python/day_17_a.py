#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      17.12.23
   Kurs:      Advent of Code
   Topic:     Clumsy Crucible
"""


from collections import defaultdict
import heapq as heap
import matplotlib.pyplot as plt

def visualize_path_with_grid(grid, shortest_path):
    rows, cols = len(grid), len(grid[0])
    plt.figure(figsize=(5,5))

    # Plot the grid values
    for i in range(rows):
        for j in range(cols):
            plt.text(j, rows - 1 - i, str(grid[i][j]), ha='center', va='center', color='black')
    # Plot the shortest path
    x, y = zip(*[(rows - 1 - i, j) for i, j in shortest_path])
    plt.plot(y, x, marker='.', linestyle='-', color='r', markersize=5)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    plt.pause(0.01)
    plt.close("all")

def convert_grid_to_graph(grid):
    rows, cols = len(grid), len(grid[0])
    graph = defaultdict(dict)
    for i in range(rows):
        for j in range(cols):
            #print(grid[i][j])
            current_node = (j,i)

            # Check neighbors (up, down, left, right)
            neighbors = [
                (j, i - 1),  # up
                (j, i + 1),  # down
                (j - 1, i),  # left
                (j + 1, i)   # right
            ]

            for neighbor_j, neighbor_i in neighbors:
                if 0 <= neighbor_i < cols and 0 <= neighbor_j < rows:
                    neighbor_node = (neighbor_j, neighbor_i)
                    cost = grid[neighbor_i][neighbor_j]
                    graph[current_node][neighbor_node] = cost

    return graph

def extract_shortest_path(parents_map, destination):
    path = [destination]
    current_node = destination

    while current_node in parents_map:
        current_node = parents_map[current_node]
        path.append(current_node)

    return list(reversed(path))

def check_repetitions(path, source):
    U = 0
    R = 0
    D = 0
    L = 0
    prev_node_x, prev_node_y = source

    for node in path:
        if node != source:
            dx = node[0] - prev_node_x
            dy = node[1] - prev_node_y

            if dx == 0 and dy < 0:
                U += 1
                R = D = L = 0
            elif dx == 0 and dy > 0:
                D += 1
                U = R = L = 0
            elif dy == 0 and dx > 0:
                R += 1
                L = D = U = 0
            elif dy == 0 and dx < 0:
                L += 1
                R = D = U = 0

            prev_node_x, prev_node_y = node

    return any(i > 3 for i in [U, L, D, R])


def dijkstra(G, source, dest, gridsize):
    m, n = gridsize
    visited = set()
    parents_map = {}
    pq = []
    node_costs = defaultdict(lambda: float('inf'))
    node_costs[source] = 0
    heap.heappush(pq, (0, source))
    node = source

    while pq:

        _, node = heap.heappop(pq)
        shortest_path = extract_shortest_path(parents_map, node)
        if node != (0,0):
            pass
        if check_repetitions(shortest_path, source):
            continue

        visited.add(node)
        for adj_node, weight in G[node].items():
            if adj_node in visited:
                continue

            new_cost = node_costs[node] + weight
            if node_costs[adj_node] > new_cost:
                parents_map[adj_node] = node
                node_costs[adj_node] = new_cost
                heap.heappush(pq, (new_cost, adj_node))

    return parents_map, node_costs

with open("data/day_17.txt") as f:
    lines = f.readlines()
L = []
for r in lines:
    L.append([int(c) for c in r.strip()])
gridsize = (len(L), len(L[0]))
graph = convert_grid_to_graph(L)
parents, node_costs = dijkstra(graph, (0, 0), (12,12), gridsize)
target = (gridsize[1] - 1, gridsize[0] - 1)
shortest_path = extract_shortest_path(parents, (9,12))
cost = 0
for s in shortest_path:
    cost += L[s[1]][s[0]]
print(shortest_path)
print(cost)
visualize_path_with_grid(L, shortest_path)



# 1264 is too high