import os
from queue import Queue
import itertools

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

def findStart(maze):
    for row, line in enumerate(maze):
        col=line.find("S")
        if col!=-1:
            return col, row
    raise ValueError("'S' not found in maze")

def determinePipeType(maze, col, row):
    up=maze[row-1][col] if row>0 else None
    down=maze[row+1][col] if row<len(maze)-1 else None
    left=maze[row][col-1] if col>0 else None
    right=maze[row][col+1] if col<len(maze[0])-1 else None
    if up in "|F7" and right in "-7J": return 'L'
    elif up in "|F7" and left in "-LF": return 'J'
    elif down in "|LJ" and right in "-7J" or down not in "|LJ" or left not in "-LF": return 'F'
    else: return '7'

def findLoop(maze, startCol, startRow):
    pipeType=determinePipeType(maze, startCol, startRow)
    queue=Queue()
    loopTiles={(startCol, startRow)}
    for moveX, moveY in ADJ_PATHS[pipeType]:
        nextCol, nextRow=startCol+moveX, startRow+moveY
        if (nextCol, nextRow) not in loopTiles:
            queue.put((1, (nextCol, nextRow)))
            loopTiles.add((nextCol, nextRow))
    while not queue.empty():
        _, (col, row)=queue.get()
        for moveX, moveY in ADJ_PATHS[maze[row][col]]:
            nextCol, nextRow = col + moveX, row + moveY
            if (nextCol, nextRow) not in loopTiles:
                queue.put((1, (nextCol, nextRow)))
                loopTiles.add((nextCol, nextRow))
    return loopTiles

def countEnclosedTiles(maze, loopTiles):
    mazeWidth, mazeHeight=len(maze[0]), len(maze)
    enclosedCount=0
    for row, col in itertools.product(range(mazeHeight), range(mazeWidth)):
        if (col, row) in loopTiles: continue
        crossCount=0
        crossCol, crossRow=col, row
        while crossCol<mazeWidth and crossRow<mazeHeight:
            if (crossCol, crossRow) in loopTiles and maze[crossRow][crossCol] not in ("L", "7"):
                crossCount+=1
            crossCol+=1
            crossRow+=1
        if crossCount%2==1: enclosedCount+=1
    return enclosedCount

if __name__=="__main__":
    path=os.path.join(os.path.dirname(__file__),'input')
    maze=read(path)
    startCol, startRow=findStart(maze)
    loopTiles=findLoop(maze, startCol, startRow)
    enclosed=countEnclosedTiles(maze, loopTiles)
    print(f"Enclosed tiles: {enclosed}")
