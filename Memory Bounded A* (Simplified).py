import heapq

def memory_bounded_a_star(graph, start, goal, h, memory_limit):
    open_list = []
    heapq.heappush(open_list, (0 + h(start), 0, start))
    came_from = {start: None}
    g_score = {start: 0}
    closed_list = set()

    while open_list:
        if len(closed_list) > memory_limit:
            closed_list.pop()

        _, current_g, current = heapq.heappop(open_list)
        closed_list.add(current)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor, cost in graph[current]:
            tentative_g = current_g + cost
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h(neighbor)
                heapq.heappush(open_list, (f_score, tentative_g, neighbor))

    return None

graph = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('E', 5), ('F', 12)],
    'C': [('G', 2)],
    'D': [],
    'E': [],
    'F': [('G', 3)],
    'G': []
}

def heuristic(n):
    H = {
        'A': 10,
        'B': 6,
        'C': 4,
        'D': 7,
        'E': 5,
        'F': 3,
        'G': 0
    }
    return H[n]

print(memory_bounded_a_star(graph, 'A', 'G', heuristic, memory_limit=5))
