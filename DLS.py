graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}



def dls(graph, start, goal, depth_limit, visited=[], depth=0, path=[]):
    visited.append(start)
    path.append(start)
    print(f"Current Node : {start}\nPath : {visited}  ")
    if start == goal:
        return path
    if depth < depth_limit:
        for neighbour in graph.get(start, []):
            if neighbour not in visited:
                new_path = dls(graph, neighbour, goal, depth_limit, visited, depth + 1, path)
                if new_path is not None:
                    path.clear()
                    visited.clear()
                    return new_path
                else:
                    path.clear()
                    visited.pop()
    else:
        print("CEHEC")

if __name__ == "__main__":
    depth_limit = 3
    path = dls(graph, "A", "E", 2)
