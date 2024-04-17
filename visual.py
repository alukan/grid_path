# N = int(input())
# arr = []
# s_pos = (0, 0)
# t_pos = (0, 0)
# for i in range(N):
#     arr.append(input())
#     for j in range(len(arr[i])):
#         if arr[i][j] == 'S':
#             s_pos = (i, j)
#         elif arr[i][j] == 'T':
#             t_pos = (i, j)

# print(t_pos, s_pos)

import heapq

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(n, grid, start, target):

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    pq = []
    heapq.heappush(pq, (0, start, [start]))  # (cost, position, path)
    visited = set()
    visited.add(start)

    while pq:
        current_cost, (x, y), path = heapq.heappop(pq)

        if (x, y) == target:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                next_cost = current_cost + 1
                distans = manhattan_distance(nx, ny, *target)
                heapq.heappush(pq, (next_cost + distans, (nx, ny), path + [(nx, ny)]))

    return []

def print_path(grid, path):
    path_set = set(path)
    path_directions = {path[i]: path[i + 1] for i in range(len(path) - 1)}

    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if (i, j) in path_set:
                if char in 'ST':
                    print('🚩', end='')
                else:
                    next_pos = path_directions[(i, j)]
                    if next_pos == (i, j + 1):
                        print('➡️', end=' ')
                    elif next_pos == (i, j - 1):
                        print('⬅️', end=' ')
                    elif next_pos == (i - 1, j):
                        print('⬆️', end=' ')
                    elif next_pos == (i + 1, j):
                        print('⬇️', end=' ')
            elif char == '#':
                print('🧱', end='')
            else:
                print('🟩', end='')
        print()

def main():
    
    N = 0
    grid = []
    start = (0, 0)
    target = (0, 0)

    with open('test/test4.txt', 'r') as file:
        N = int(file.readline().strip())
        for i in range(N):
            line = file.readline().strip()
            grid.append(line)
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i, j)
                elif line[j] == 'T':
                    target = (i, j)


    path = a_star_search(N, grid, start, target)
    print_path(grid, path)

if __name__ == "__main__":
    main()
