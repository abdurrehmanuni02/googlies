def DFS(graph, start, goal):
    stack = [(start, [start])]
    tested = {start}

    while stack:
        hooked_node = stack.pop()
        node = graph[hooked_node[0]]
        if hooked_node[0] == goal:
            return hooked_node[1]
        for child in node:
            if child in tested:
                continue
            else:
                stack.append((child, hooked_node[1] + [child]))
                tested.add(child)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Final Path : " , DFS(graph , 'B', 'F'))