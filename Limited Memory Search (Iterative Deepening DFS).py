def iddfs(graph, start, goal):
    def dls(node, goal, depth):
        if depth == 0:
            return node == goal
        if depth > 0:
            for neighbor in graph[node]:
                if dls(neighbor, goal, depth - 1):
                    return True
        return False

    for depth in range(len(graph)):
        if dls(start, goal, depth):
            return True
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(iddfs(graph, 'A', 'F'))
