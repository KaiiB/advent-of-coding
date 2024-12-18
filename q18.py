from collections import deque

grid = [[0 for _ in range(71)] for _ in range(71)]
directions = ((0, -1), (0, 1), (-1, 0), (1, 0))

with open('./q18_input.txt') as f:
    lines = f.readlines()[::-1]
    for i in range(1024):
        coords = lines.pop().strip().split(',')
        grid[int(coords[0])][int(coords[1])] = 1

def bfs():
    q = deque()
    visited = set()
    q.append((0, 0, 0))
    while q:
        r, c, level = q.popleft()
        if r == 70 and c == 70:
            return level
        for dr, dc in directions:
            if (r + dr, c + dc) not in visited and min(r + dr, c + dc) >= 0 and r + dr < 71 and c + dc < 71 and grid[r + dr][c + dc] == 0:
                visited.add((r + dr, c + dc))
                q.append((r + dr, c + dc, level + 1))
    return -1

def find_false_coord():
    while lines:
        coords = lines.pop().strip().split(',')
        grid[int(coords[0])][int(coords[1])] = 1
        if bfs() == -1:
            return coords
            
print(bfs())
print(find_false_coord())

print('done')
        