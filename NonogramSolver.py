"""
print_grid(): Simple function that takes 2D array as an input and prints each row one by one to present a square grid in the console
"""
def print_grid(grid):
    for r in range(len(grid)):
        print(grid[r])

class Nonogram:

    def __init__(self, grid_size, valid_rows, valid_cols):
        self.grid = [[None for i in range(grid_size)] for j in range(grid_size)] # Initializes the 2D Array which will contain the grid itself
        self.valid_rows = valid_rows
        self.valid_cols = valid_cols

    







    """
    nonogram_solver(): The main function that will do the solving of the puzzle. I am going to take a recursive backtracking approach in order to fill in the each
                       cell of the grid. If it encounters a conflict it will go back and try a different value for the cell and will continue until it reaches the last index.

    """
    def nonogram_solver(self):

      return self.grid