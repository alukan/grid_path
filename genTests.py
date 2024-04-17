import os
import random
from collections import deque

def gen_grid(n):
    grid = [[random.choice(['#', '.']) for _ in range(n)] for _ in range(n)]
    
    def dfs(x, y, target, path):
        if (x, y) == target:
            return True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in path:
                path.add((nx, ny))
                if dfs(nx, ny, target, path):
                    return True
                path.remove((nx, ny))
        return False

    start = (random.randint(0, n-1), random.randint(0, n-1))
    target = (random.randint(0, n-1), random.randint(0, n-1))
    while target == start:
        target = (random.randint(0, n-1), random.randint(0, n-1))

    grid[start[0]][start[1]] = '.'
    grid[target[0]][target[1]] = '.'

    path = set([start])
    if not dfs(start[0], start[1], target, path):
        return gen_grid(n)

    for (x, y) in path:
        grid[x][y] = '.'
    grid[start[0]][start[1]] = 'S'
    grid[target[0]][target[1]] = 'T'

    return grid

def save_grid(grid, filename):
    with open(filename, 'w') as file:
        file.write(str(len(grid)) + "\n")
        for row in grid:
            file.write("".join(row) + "\n")

def main():
    min_size = int(input('Enter minimum size: '))
    max_size = int(input('Enter maximum size: '))
    num_tests = int(input('Enter number of tests: '))
    
    for i in range(num_tests):
        size = random.randint(min_size, max_size)
        grid = gen_grid(size)
        
        os.makedirs(f'test/', exist_ok=True)
        
        save_grid(grid, f'test/test{i}.txt')
        

if __name__ == '__main__':
    main()
