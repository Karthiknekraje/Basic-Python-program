import heapq

def heuristic(state, goal):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                h += 1
    return h

def get_neighbors(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
    neighbors = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def a_star(start, goal):
    frontier = [(heuristic(start, goal), 0, start, [])]
    explored = set()
    while frontier:
        _, cost, state, path = heapq.heappop(frontier)
        if state == goal:
            return path + [state]
        explored.add(tuple(map(tuple, state)))
        for neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in explored:
                heapq.heappush(frontier, (cost + 1 + heuristic(neighbor, goal), cost + 1, neighbor, path + [state]))
    return None

start = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

solution = a_star(start, goal)
for step in solution:
    for row in step:
        print(row)
    print()
