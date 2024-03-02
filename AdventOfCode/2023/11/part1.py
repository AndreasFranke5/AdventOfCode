import os

def read(path):
    with open(path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def expandGrid(grid):
    def onlyDots(line):
        return all(cell == '.' for cell in line)
    
    makeGrid=[]
    for row in grid:
        makeGrid.append(row.copy())
        if onlyDots(row):
            makeGrid.append(row.copy())
    
    grid=makeGrid
    gridTransposed=list(map(list, zip(*grid)))
    makeGridTransposed=[]
    for col in gridTransposed:
        makeGridTransposed.append(col)
        if onlyDots(col):
            makeGridTransposed.append(list(col))
    
    gridFinal=list(map(list,zip(*makeGridTransposed)))
    return gridFinal

def mDist(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def distSum(grid):
    id=1
    pos={}
    for i,row in enumerate(grid):
        for j,cell in enumerate(row):
            if cell == '#':
                grid[i][j]=id
                pos[id]=(i,j)
                id+=1
    
    dists=[]
    for id1,pos1 in pos.items():
        for id2,pos2 in pos.items():
            if id1<id2:
                dist=mDist(pos1,pos2)
                dists.append(dist)
    
    return sum(dists)

path=os.path.join(os.path.dirname(__file__), 'input')
grid=read(path)

expandedGrid=expandGrid(grid)
totalDist=distSum(expandedGrid)

for row in expandedGrid:
    print(''.join(str(cell) for cell in row))

print(f"Total distance: {totalDist}")
