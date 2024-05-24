# generate_maze.py

import random

# Function to find valid neighbour
def find_neighbors(x, y, width, height, maze):
    neighbors = []
    if x > 1 and maze[y][x - 2] == 'W':
        neighbors.append((x - 2, y))
    if x < width - 2 and maze[y][x + 2] == 'W':
        neighbors.append((x + 2, y))
    if y > 1 and maze[y - 2][x] == 'W':
        neighbors.append((x, y - 2))
    if y < height - 2 and maze[y + 2][x] == 'W':
        neighbors.append((x, y + 2))
    return neighbors

# Function to connect cell
def connect_cells(maze, cell, next_cell):
    x, y = cell
    nx, ny = next_cell
    if nx == x:
        maze[min(ny, y) + 1][x] = 'P'
    else:
        maze[y][min(nx, x) + 1] = 'P'

# Function to generate maze
def generate_maze(width, height):
    maze = [['W' for _ in range(width)] for _ in range(height)]
    stack = [(1, 1)]

    while stack:
        cell = stack[-1]
        x, y = cell
        maze[y][x] = 'P'
        neighbors = find_neighbors(x, y, width, height, maze)

        if neighbors:
            next_cell = random.choice(neighbors)
            connect_cells(maze, cell, next_cell)
            stack.append(next_cell)
        else:
            stack.pop()

    # Marking the final cell
    maze[height - 2][width - 2] = 'F'

    return maze
