import os
from queue import Queue


ADJ_PATHS = {
    "F": [(1,0),(0,1)],
    "7": [(-1,0),(0,1)],
    "L": [(0,-1),(1,0)],
    "J": [(0,-1),(-1,0)],
    "|": [(0,-1),(0,1)],
    "-": [(-1,0),(1,0)],
}

def read(path):
    with open(path,'r') as file:
        return [line.strip() for line in file]

def startPos(maze):
    for y, line in enumerate(maze):
        x = line.find("S")
        if x != -1:
            return x, y
    raise ValueError("'S' not found in maze")

def queueStart(maze, start_x, start_y):
    queue=Queue()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        adjTile=maze[start_y + dy][start_x + dx]
        if adjTile in ADJ_PATHS:
            for dx2, dy2 in ADJ_PATHS[adjTile]:
                if start_x == start_x + dx + dx2 and start_y == start_y + dy + dy2:
                    queue.put((1, (start_x + dx, start_y + dy)))
    return queue

def countMaxSteps(maze, start_x, start_y):
    queue = queueStart(maze, start_x, start_y)
    visited = {(start_x, start_y): 0}
    while not queue.empty():
        dist, (x, y) = queue.get()
        if (x, y) in visited:
            continue
        visited[(x, y)] = dist
        for dx, dy in ADJ_PATHS[maze[y][x]]:
            queue.put((dist + 1, (x + dx, y + dy)))
    return max(visited.values())

if __name__=="__main__":
    path=os.path.join(os.path.dirname(__file__), 'input')
    maze=read(path)
    start_x, start_y = startPos(maze)
    maxSteps=countMaxSteps(maze, start_x, start_y)
    print(f"Maximum steps: {maxSteps}")
