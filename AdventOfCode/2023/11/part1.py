import os

def read(path):
    with open(path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def expandGrid(grid):
    def is_all_dots(line):
        return all(cell == '.' for cell in line)

    new_grid = []
    for row in grid:
        new_grid.append(row.copy())  # Copy the row to avoid modifying the original grid
        if is_all_dots(row):
            new_grid.append(row.copy())
    grid = new_grid

    transposed_grid = list(map(list, zip(*grid)))
    
    new_transposed_grid = []
    for col in transposed_grid:
        new_transposed_grid.append(col)
        if is_all_dots(col):
            new_transposed_grid.append(list(col))

    final_grid = list(map(list, zip(*new_transposed_grid)))
    return final_grid  # Keep it as a list of lists

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def distSum(grid):
    # Replace '#' with unique numbers and store their positions
    identifier = 1
    positions = {}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '#':
                grid[i][j] = identifier
                positions[identifier] = (i, j)
                identifier += 1

    # Calculate all pairwise Manhattan distances
    distances = []
    for id1, pos1 in positions.items():
        for id2, pos2 in positions.items():
            if id1 < id2:
                distance = manhattan_distance(pos1, pos2)
                distances.append(distance)

    # Sum up all distances
    return sum(distances)

path = os.path.join(os.path.dirname(__file__), 'input')
grid = read(path)

expandedGrid = expandGrid(grid)
totalDist = distSum(expandedGrid)

for row in expandedGrid:
    print(''.join(str(cell) for cell in row))  # Convert each cell to string for printing

print(f"Total distance: {totalDist}")
