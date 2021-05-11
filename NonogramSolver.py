"""
main(): The main method that will be executed at the end of the file. Will contain the code that sets up the 2D-array that we are going to fill in with 1s and
        0s in order to display the properly solved puzzle. Additionally, it will hold the clues for each row and column that the algorithm will use to find out
        the correct solution of the puzzle. Lastly, it will call the solver function and then display the solved puzzle.

"""
def main():
    grid_dim = 5 
    puzzle_grid = [[None for i in range(grid_dim)] for j in range(grid_dim)] # Initializes the 2D Array which will contain the grid itself
    valid_rows = [[3,1], [1,1,1], [5], [2], [4]] # Array containing the correct number of "filled-in" squares for the rows of the grid
    valid_cols = [[3], [1,3], [5], [1,1], [3,1]] # Array containing the correct number of "filled-in" squares for the columns of the grid
    

    return 0



"""
nonogram_solver(): The main function that will do the solving of the puzzle. I am going to take a recursive backtracking approach in order to fill in the each
                   cell of the grid. If it encounters a conflict it will go back and try a different value for the cell and will continue until it reaches the last index.

"""
def nonogram_solver(puzzle_grid, valid_rows, valid_cols):
    

    return puzzle_grid





main()