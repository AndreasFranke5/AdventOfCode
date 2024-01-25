import os

def read(path):
    with open(path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def count_empty_lines(grid):
    empty_rows = [i for i, row in enumerate(grid) if all(cell == '.' for cell in row)]
    empty_cols = [j for j in range(len(grid[0])) if all(grid[i][j] == '.' for i in range(len(grid)))]
    return empty_rows, empty_cols

def calculate_total_distance(grid, expansion_factor=1000000):
    empty_rows, empty_cols = count_empty_lines(grid)

    # Store positions of '#'
    positions = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '#']

    total_distance = 0
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            p1, p2 = positions[i], positions[j]
            row_dist = abs(p1[0] - p2[0])
            col_dist = abs(p1[1] - p2[1])

            # Adjust distance for empty rows and columns
            row_dist_adjusted = row_dist + sum(bool(r in empty_rows)
                                           for r in range(min(p1[0], p2[0]), max(p1[0], p2[0]))) * (expansion_factor - 1)
            col_dist_adjusted = col_dist + sum(1 for c in range(min(p1[1], p2[1]), max(p1[1], p2[1])) if c in empty_cols) * (expansion_factor - 1)

            total_distance += row_dist_adjusted + col_dist_adjusted

    return total_distance

path = os.path.join(os.path.dirname(__file__), 'input')
grid = read(path)
total_distance = calculate_total_distance(grid)
print(f"Total distance: {total_distance}")
