graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}


def iddfs(graph, start, goal ):
    depth_limit = 0
    while True:
        path = dls(graph, start, goal, depth_limit, visited=[], path=[])
        if path is not None:
            return path
        depth_limit += 1


def dls(graph, start, goal, depth_limit, visited=[], path=[]):
    visited.append(start)
    path.append(start)
    print(f"Current Node : {start}\nPath : {visited}  ")
    if start == goal:
        return path
    if depth_limit == 0:
        return None
    if depth_limit > 0:
        for neighbour in graph.get(start, []):
            if neighbour not in visited:
                new_path = dls(graph, neighbour, goal, depth_limit-1, visited, path)
                if new_path is not None:
                    return new_path
                else:
                    visited.pop()




if __name__ == "__main__":
    depth_limit = 3
    path = iddfs(graph, "A", "C")
