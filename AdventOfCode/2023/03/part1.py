import re
import os

# Created a 140 x 140 grid for the input file, then checked each cell at row and col +/-1 for adjacency.
def read(path):
    with open(path,"r") as file:
        c=file.readlines()
    grid=[list(row.rstrip('\n')) for row in c]
    symbol=[]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if not grid[row][col].isdigit() and grid[row][col]!='.':
                symbol.append((row,col))
    return grid,symbol

def adjacency(grid, symbol):
    adjacent=set()
    rows, cols = len(grid), len(grid[0])
    for row, col in symbol:
        if grid[row][col] == '.':
            continue
        for adjacent_col in range(max(0, col-1), min(cols, col+2)):
            if grid[row][adjacent_col].isdigit():
                adjacent.add((row, adjacent_col))
        for adjacent_row in [row-1, row+1]:
            if 0<=adjacent_row<rows:
                for adjacent_col in range(max(0, col-1), min(cols, col+2)):
                    if grid[adjacent_row][adjacent_col].isdigit():
                        adjacent.add((adjacent_row, adjacent_col))
    return adjacent

def result(grid,adjacent):
    total=0
    pattern=re.compile(r'\d+')
    for row in range(len(grid)):
        r=''.join(grid[row])
        for found_match in pattern.finditer(r):
            firstpos,lastpos=found_match.span()
            if any((row,col) in adjacent for col in range(firstpos,lastpos)):
                total+=int(found_match.group())
    return total

path=os.path.join(os.path.dirname(__file__),'input')
grid,symbol=read(path)
adjacent_nums=adjacency(grid,symbol)
print(f"Sum: {result(grid,adjacent_nums)}")