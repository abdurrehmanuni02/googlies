from queue import PriorityQueue

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
    workspace = PriorityQueue()  # Create priority queue instance
    workspace.put((heuristic[start], [start]))  # Initialize with start node and heuristic value
    explored = set()

    while not workspace.empty():
        cost, path = workspace.get()  # Retrieve path with lowest heuristic value
        current = path[-1]
        if current == goal:
            return path, cost
        explored.add(current)
        neighbours = graph[current]
        for neighbour, pathCost in neighbours.items():
            if neighbour not in explored:
                new_cost = cost + pathCost + heuristic[neighbour]
                new_path = path + [neighbour]
                workspace.put((new_cost, new_path))  # Add new path to priority queue with updated cost

print(hill_start("A", "E"))

