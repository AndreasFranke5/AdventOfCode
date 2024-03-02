import os

def read(path):
    with open(path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def emptyLineCount(grid):
    eRow=[i for i, row in enumerate(grid) if all(cell == '.' for cell in row)]
    eCol=[j for j in range(len(grid[0])) if all(grid[i][j] == '.' for i in range(len(grid)))]
    return eRow,eCol

def calculateDistance(p1, p2, eRow, eCol, expand):
    dRow=abs(p1[0]-p2[0])
    dCol=abs(p1[1]-p2[1])
    dRowNew=dRow+sum(bool(r in eRow) for r in range(min(p1[0],p2[0]),max(p1[0],p2[0])))*(expand-1)
    dColNew=dCol+sum(1 for c in range(min(p1[1], p2[1]), max(p1[1], p2[1])) if c in eCol)*(expand-1)
    return dRowNew+dColNew

def distSum(grid,expand=1000000):
    eRow,eCol=emptyLineCount(grid)
    pos=[(i,j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '#']
    totalDist=0
    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            p1,p2=pos[i],pos[j]
            totalDist+=calculateDistance(p1,p2,eRow,eCol,expand)
    return totalDist

path=os.path.join(os.path.dirname(__file__), 'input')
grid=read(path)

totalDist=distSum(grid)
print(f"Total distance: {totalDist}")
