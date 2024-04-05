
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


def dfs(graph, start):
    stack = [start]
    visited = set()
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            print("Visited Node:", current)
            for neighbor in graph[current]:
                stack.append(neighbor)

if __name__ == "__main__":
    start_node = 'A'
    dfs(graph, start_node)


