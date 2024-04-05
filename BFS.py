from collections import deque
def BFS(graph,start,goal):
    queue = deque([(start,[start])])
    tested = set([start])
    
    while queue:
        hookedNode = queue.popleft()
        node = graph[hookedNode[0]]
        if hookedNode[0] == goal:
            return hookedNode[1]
        for child in node:
            if child in tested:
                continue
            else:
                queue.append((child ,hookedNode[1]+[child]))
                tested.add(child)





graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Final Path : " , BFS(graph , 'B', 'F'))
