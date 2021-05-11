class Nonogram:

    def __init__(self, grid_size, valid_rows, valid_cols):
        self.grid_size = grid_size
        self.grid = [[0 for i in range(grid_size)] for j in range(grid_size)] # Initializes the 2D Array which will contain the grid itself
        self.valid_rows = valid_rows
        self.valid_cols = valid_cols

    def __repr__(self):
        s = "\n"
        for r in range(len(self.grid)):
            s += str(self.grid[r])
            s += "\n"
        return s

    def is_valid_row(self, row_index):
        correct_row_values = self.valid_rows[row_index]
        current_block_size = 0
        starting_index = 0
        for i in range(len(correct_row_values)):
            for j in range(starting_index, len(self.grid)):
                # Handles cases of 0s in the current cell
                if self.grid[row_index][j] == 0 and current_block_size != 0: # Case 1: There is a 0 interrupting what should be a continuous block. Thus, the row is invalid and the method returns False.
                    return False
                if self.grid[row_index][j] == 0 and current_block_size == 0: # Case 2: There is a 0 but there is not a continuous block so it iterates to next index
                    continue
                # Handles cases of 1s in the current cell
                if self.grid[row_index][j] == 1 and current_block_size > correct_row_values[i]: # Case 1: There is a 1, making the block too long. Thus, the row is invalid and the method returns False.
                    return False
                if self.grid[row_index][j] == 1 and current_block_size < correct_row_values[i]: # Case 2: There is a 1 and the block isn't large enough yet, adds to the counter for block size.
                    current_block_size += 1
                # Checks if the current block is satisfied. Resets the block size counter and sets the starting index for the loop to the next index in the array.
                if current_block_size == correct_row_values[i]:
                    current_block_size = 0
                    starting_index = j+1
                    if starting_index >= len(self.grid) and i == len(correct_row_values) - 1: # Checks if starting index is out of bounds and if we are checking the last block. If both are true then the row is valid and the method return True.
                        return True
                    elif self.grid[row_index][starting_index] == 1: # Since the if statement above failed, we check if the next index is a 1, if it is then the block is too long and the method return False.
                        return False
                    else: # If we hit this else statement, then we have another block to check and we break out of the inner loop to check the next block.
                        break
        if 1 in self.grid[row_index][starting_index:]:
            return False # If there is another 1 found passed the loop, then there is an extra block and the method returns False.
        else:
            return True # If we finished iterating through all of the row values and indices in the row then the row is valid and the method returns True.

    def is_valid_col(self, col_index):
        correct_col_values = self.valid_cols[col_index]
        current_block_size = 0
        starting_index = 0
        for i in range(len(correct_col_values)):
            for j in range(starting_index, len(self.grid[0])):
                # Handles cases of 0s in the current cell
                if self.grid[j][col_index] == 0 and current_block_size != 0: # Case 1: There is a 0 interrupting what should be a continuous block. Thus, the column is invalid and the method returns False.
                    return False
                if self.grid[j][col_index] == 0 and current_block_size == 0: # Case 2: There is a 0 but there is not a continuous block so it iterates to next index
                    continue
                # Handles cases of 1s in the current cell
                if self.grid[j][col_index] == 1 and current_block_size > correct_col_values[i]: # Case 1: There is a 1, making the block too long. Thus, the column is invalid and the method returns False.
                    return False
                if self.grid[j][col_index] == 1 and current_block_size < correct_col_values[i]: # Case 2: There is a 1 and the block isn't large enough yet, adds to the counter for block size.
                    current_block_size += 1
                # Checks if the current block is satisfied. Resets the block size counter and sets the starting index for the loop to the next index in the array.
                if current_block_size == correct_col_values[i]:
                    current_block_size = 0
                    starting_index = j+1
                    if starting_index >= len(self.grid[0]) and i == len(correct_col_values) - 1: # Checks if starting index is out of bounds and if we are checking the last block. If both are true then the column is valid and the method return True.
                        return True
                    elif self.grid[starting_index][col_index] == 1: # Since the if statement above failed, we check if the next index is a 1, if it is then the block is too long and the method return False.
                        return False
                    else: # If we hit this else statement, then we have another block to check and we break out of the inner loop to check the next block.
                        break
        for j in range(starting_index, len(self.grid[0])): # Loops through the remaining indices checking if there is an extra block. Returns False if there is
            if self.grid[j][col_index] == 1:
                return False 

        else:
            return True # If we finished iterating through all of the column values and indices in the column then the column is valid and the method returns True.





    """
    nonogram_solver(): The main function that will do the solving of the puzzle. I am going to take a recursive backtracking approach in order to fill in the each
                       cell of the grid. If it encounters a conflict it will go back and try a different value for the cell and will continue until it reaches the last index.

    """
    def nonogram_solver(self, n):

      return self.grid
      


test_rows = [[3,1], [1,1,1], [5], [2], [4]] # Array containing the correct number of "filled-in" squares for the rows of the grid
test_cols = [[3], [1,3], [5], [1,1], [3,1]] # Array containing the correct number of "filled-in" squares for the columns of the grid
NonogramTest = Nonogram(5, test_rows, test_cols)

print(NonogramTest)