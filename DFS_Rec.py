graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = []
        path = []

    path.append(start)
    stack = [start]
    visited.append(start)
    if start == goal:
        return path
    while stack:
        current = stack.pop()
        for n in graph[current]:
            if n not in visited:
                stack.append(n)
                new_path = dfs(graph, n, goal, visited[:], path[:])
                if new_path is not None:
                    path.clear()
                    return new_path


if __name__ == "__main__":
    path = dfs(graph, "A", "F")
    print(path)
