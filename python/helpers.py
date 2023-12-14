import matplotlib.pyplot as plt
import numpy as np
import networkx as nx



def visualize_graph(graph, grid_size, symbols, edges):
    # Extract grid dimensions
    m, n = grid_size

    pos = {(x, y): (y, -x) for x, y in graph.nodes()}

    # print(graph.nodes)

    labels = {node: symbols[node] for node in graph.nodes}

    start_node = None
    node_color = ['red' if start_node else 'skyblue' for node in graph.nodes]

    # print(edges)

    # edge_color = ['darkgreen' if (u, v) in edges or (
    #     v, u) in edges else 'lightgray' for u, v in graph.edges]

    # Draw the graph using the grid layout
    nx.draw(graph, pos=pos, with_labels=True, labels=labels, font_weight='bold', node_size=140,
            node_color=node_color, font_color='black', font_size=12, edgelist=edges, edge_color="red", width=4)

    # Show the plot
    plt.show()


def insert_to_numpy(M):
    increase_idx_by = 0
    for i, row in enumerate(M):
        if np.all(row == '.'):
            M = np.insert(M, i+increase_idx_by, row, axis=0)
            increase_idx_by += 1
    increase_idx_by = 0
    for i, column in enumerate(M.T):
        if np.all(column == '.'):
            M = np.insert(M, i+increase_idx_by, column, axis=1)
            increase_idx_by += 1
    return M
