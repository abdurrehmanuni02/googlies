from collections import deque
def UCS(graph,start,goal):
    cost = 0
    queue = deque([(start,[{start:0}])])
    tested = set([start])
    allPaths=[]

    while queue:
       
        hookedNode = queue.popleft()
        node = graph[hookedNode[0]]
        if hookedNode[0] == goal:
            allPaths.append(hookedNode[1])
        for child in node:   
           queue.append((list(child.keys())[0] ,hookedNode[1]+[child]))
           tested.add(list(child.keys())[0])
    for path in allPaths:   
        cost=0
        for c in path:
            cost+=list(c.values())[0]
        path.append(cost)
        print(path)

    



#main
graph = {
    'A': [{'B' : 2}, {'C' : 4}],
    'B': [{'D': 6}, {'E' : 9}],
    'C': [{'F':5}],
    'D': [],
    'E': [{'F' : 1}],
    'F': []
}

UCS(graph , 'A', 'F')
