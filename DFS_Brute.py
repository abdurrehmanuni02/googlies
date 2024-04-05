from collections import deque


def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    while stack:
        # print(stack)
        node = stack.pop()
        print(node, end=" ")
        if node == goal:
            return
        for neigh in graph[node]:
            if neigh not in visited:
                stack.append(neigh)
                visited.add(neigh)


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}
dfs(graph, "A", "F")
