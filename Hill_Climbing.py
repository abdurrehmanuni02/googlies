graph = {
    'A': {'B': 1, 'C': 3, 'D': 7},
    'B': {'A': 1, 'C': 1, 'E': 5},
    'C': {'A': 3, 'B': 1, 'D': 2, 'E': 3},
    'D': {'A': 7, 'C': 2, 'E': 1},
    'E': {'B': 5, 'C': 3, 'D': 1}
}
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 0
}


def hill_start(start, goal):
    workspace = [(heuristic[start], [start])]
    explored = set()

    while workspace:
        workspace.sort(key=lambda x: x[0])
        print(workspace)
        cost, path = workspace.pop(0)
        current = path[-1]
        if current == goal:
            return path, cost
        explored.add(current)
        neighbours = graph[current]
        for neighbour, pathCost in neighbours.items():
            if neighbour not in explored:
                new_cost = cost + pathCost + heuristic[neighbour]
                new_path = path + [neighbour]
                workspace.append((new_cost, new_path))


print(hill_start("B", "D"))
