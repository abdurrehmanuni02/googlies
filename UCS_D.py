graph = {
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


def ucs(graph, start, goal):
    visited = set()
    pq = [(0, start, [start])]
    while pq:
        pq = sorted(pq, key=lambda x: x[0])
        cost, current, path = pq.pop(0)
        if current not in visited:
            visited.add(current)
            if current == goal:
                return path
            for neighbour, edge_cost in graph[current]:
                if neighbour not in visited:
                    pq.append((cost + edge_cost, neighbour, path + [neighbour]))


if __name__ == "__main__":
    start_node = 'Iasi'
    goal_node = 'Eforie'
    path = ucs(graph, start_node, goal_node)
    print("Path:", path)