def iddfs(graph, start, goal):
    depth_limit = 0
    while True:
        path = dldfs(graph, start, goal, depth_limit, [])
        if path is not None:
            return path
        depth_limit += 1


def dldfs(graph, start, goal, depth_limit, visited=[]):
    if start not in graph.keys() or goal not in graph.keys():
        return None

    visited.append(start)
    print("Current Node:", start)

    if start == goal:
        return visited

    if depth_limit == 0:
        return None

    if depth_limit > 0:
        for child in graph[start]:
            if child not in visited:
                path = dldfs(graph, child, goal, depth_limit - 1, visited[:])
                if path is not None:
                    return path

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = 'E'

path = iddfs(graph, start_node, goal_node)
if path:
    print("Path found:", path)
else:
    print("No path found within depth limit")