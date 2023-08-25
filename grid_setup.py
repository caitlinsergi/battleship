def initialize_empty_grid():
    grid_length = 8
    grid = {'': "  A B C D E F G H"}
    for row_num in range(1, grid_length +1):
        grid[str(row_num)] = "|_" * grid_length
    return grid

def print_grid(grid):
    for keys, values in grid.items():
        print(keys, values)


