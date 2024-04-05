from collections import deque
from queue import PriorityQueue

#BFS
def bfs(graph,start,goal):
    if start not in graph.keys() or goal not in graph.keys():
        print("Start or Goal are not in graph")
        return
    visited = set()
    queue = deque()
    queue.append((start,[start]))
    visited.add(start)
    while queue:
        node,path = queue.popleft()

        if node == goal:
            return path

        for child in graph[node]:
            if child not in visited:
                queue.append((child,path + [child]))
                visited.add(child)


#DFS recursive
def dfs_recursive(graph, start, goal, visited=[]):
    if start not in graph.keys() or goal not in graph.keys():
        print("Start or Goal are not in graph")
        return
    visited.append(start)
    if start == goal:
        return visited
    for child in graph[start]:
        if child not in visited:
            path = dfs_recursive(graph, child, goal, visited)
            if path is not None:
                return path
            visited.pop()

#DFS stack
def dfs_stack(graph,start,goal):
    if start not in graph.keys() or goal not in graph.keys():
        print("Start or Goal are not in graph")
        return
    visited = set()
    stack = deque()
    stack.appendleft((start,[start]))

    while stack:
        # print("Stack ", stack)
        node,path= stack.popleft()
        # print(f"Current Node : {node} : Path {path}")
        visited.add(node)
        if node == goal:
            return path
        for child in graph[node]:
            if child not in visited:
                stack.appendleft((child,path+[child]))


#DFS depth limit search using recursion
def depth_limit_search_recursion(graph,start,goal,visited=[],current_depth=0,depth_limit = 6):
    if start not in graph.keys() or goal not in graph.keys():
        print("Start or Goal are not in graph")
        return
    visited.append(start)
    print(f"Current Node : {start}\nPath : {visited}")
    if start == goal:
        return visited
    if current_depth<depth_limit:
        for child in graph[start]:
            if child not in visited:
              path = depth_limit_search_recursion(graph,child,goal,visited,current_depth+1,depth_limit)
              if path is not None:
                  return  path
              visited.pop()


#DFS iterative
# Start Point of iterative deepening
def iddfs(graph,start,goal):
    depth_limit = 0
    while True:
        path=dldfs(graph,start,goal,depth_limit,[])
        if path is not None:
            return path
        depth_limit +=1

#Depth Limit Search for iterative Deepening Search
def dldfs(graph,start,goal,depth_limit,visited=[]):
    if start not in graph.keys() or goal not in graph.keys():
        return None
    visited.append(start)
    print("Current Node :",start)
    if start == goal:
        return visited
    if depth_limit == 0:
        return None
    if depth_limit > 0:
        for child in graph[start]:
            if child not in visited:
                path = dldfs(graph,child,goal,depth_limit-1,visited)
                if path is not None:
                    return path
                visited.pop()
# End point of iterative deepening
#UCS

def UCS(graph,start,goal):
    if start not in graph.keys() or goal not in graph.keys():
        return None

    visited = {}
    pqueue = PriorityQueue()
    pqueue.put((0,start,[start])) # (cost,node,path

    while not pqueue.empty():
        cost,node,path = pqueue.get()
        visited[node] = cost
        if node == goal:
            return path
        for childNode,childCost in graph[node]:
            new_cost = cost + childCost
            if childNode not in visited or new_cost<visited[childNode]:
                pqueue.put((new_cost,childNode,path+[childNode]))






# simple graph for BFS,DFS,Depth limit and iterative
graph = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Arad', 'Oradea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Craiova': ['Rimnicu Vilcea', 'Pitesti', 'Drobeta'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi'],
    'Eforie': ['Hirsova']
}



#weightedGraph for UCS
weightedGraph = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99),
              ('Rimnicu Vilcea', 80)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Craiova': [('Rimnicu Vilcea', 146), ('Pitesti', 138), ('Drobeta', 120)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90),
                  ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)],
    'Eforie': [('Hirsova', 86)]
}

dummy_graph = {
 'A': ['B', 'C'],
 'B': ['D'],
 'C': ['E'],
 'D': ['F'],
 'E': ['F'],
 'F': []
}
#Main
# Testing BFS
# print("BFS path  : ",bfs(graph,"Arad","Bucharest"))

#Testing DFS recursive
# print("DFS Recursive path : ", dfs_recursive(graph,"Arad","Bucharest"))

#Testing DFS using stack
# print("DFS Stack : ",dfs_stack(graph,"Arad","Bucharest"))

#Testing Depth Limit Search using stack

# print("Depth Limit Search : ",depth_limit_search_recursion(graph,"Arad","Bucharest",[],0,3))

#Testing Iterative Deepening Depth First Search
# print("Iterative Deepening DFS  : ",iddfs(graph,"Arad","Bucharest"))

#Testing UCS
# print("UCS path : ",UCS(weightedGraph,"Arad","Bucharest"))