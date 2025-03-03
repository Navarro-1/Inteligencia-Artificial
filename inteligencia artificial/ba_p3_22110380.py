import pandas as pd
import numpy as np


data = {
    'a': {'a': 0, 'b': 2, 'c': 0, 'd': 0, 'e': 0, 'f': 1, 'g': 0, 'z': 0},
    'b': {'a': 2, 'b': 0, 'c': 2, 'd': 2, 'e': 0, 'f': 0, 'g': 0, 'z': 0},
    'c': {'a': 0, 'b': 2, 'c': 0, 'd': 0, 'e': 3, 'f': 0, 'g': 0, 'z': 1},
    'd': {'a': 0, 'b': 2, 'c': 0, 'd': 0, 'e': 4, 'f': 3, 'g': 0, 'z': 0},
    'e': {'a': 0, 'b': 0, 'c': 3, 'd': 4, 'e': 0, 'f': 0, 'g': 7, 'z': 0},
    'f': {'a': 1, 'b': 0, 'c': 0, 'd': 3, 'e': 0, 'f': 0, 'g': 5, 'z': 0},
    'g': {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 7, 'f': 5, 'g': 0, 'z': 6},
    'z': {'a': 0, 'b': 0, 'c': 1, 'd': 0, 'e': 0, 'f': 0, 'g': 6, 'z': 0}
}

grafos = pd.DataFrame(data)

def dijkstra(grafos, start):
    V = grafos.columns
    dist = {v: np.inf for v in V}
    dist[start] = 0
    visited = set()
    path = {v: None for v in V}

    while len(visited) < len(V):
        min_dist_node = None
        for node in V:
            if node not in visited:
                if min_dist_node is None or dist[node] < dist[min_dist_node]:
                    min_dist_node = node

        if min_dist_node is None:
            break

        for neighbor, weight in grafos[min_dist_node].items():
            if weight > 0 and neighbor not in visited:
                new_dist = dist[min_dist_node] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    path[neighbor] = min_dist_node

        visited.add(min_dist_node)

    return dist, path

def shortest_path(paths, start, end):
    current_node = end
    path = []

    while current_node != start:
        if paths[current_node] is None:
            return None 
        path.append(current_node)
        current_node = paths[current_node]

    path.append(start)
    path.reverse()

    return path

start_node = 'a'
end_node = 'z'
distances, paths = dijkstra(grafos, start_node)

shortest_path_result = shortest_path(paths, start_node, end_node)

if shortest_path_result:
    print(f"Camino mas corto desde '{start_node}' hasta '{end_node}': {' -> '.join(shortest_path_result)}")
    print(f"Distancia total: {distances[end_node]}")
else:
    print(f"No hay un camino disponible desde '{start_node}' hasta '{end_node}'.")

