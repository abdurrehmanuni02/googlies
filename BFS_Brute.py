from collections import deque


def bfs(graph, start, goal):
    q = deque()
    q.append(start)
    visited = set()
    while q:
        print(list(q))
        node = q.popleft()
        if node[-1] == goal:
            return node
        for neigh in graph[node[-1]]:
            if neigh not in visited:
                q.append(node + neigh)
                visited.add(node)

    return "NONE"


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}
print(bfs(graph, "A", "F"))
