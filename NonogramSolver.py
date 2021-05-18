class Nonogram:

    def __init__(self, grid_size, valid_rows, valid_cols):
        self.grid_size = grid_size
        self.grid = [[0 for i in range(grid_size)] for j in range(grid_size)] # Initializes the 2D Array which will contain the grid itself
        self.valid_rows = valid_rows
        self.valid_cols = valid_cols
        self.potential_rows = {}
        for i in range(grid_size):
            self.potential_rows[i] = []

    def __repr__(self):
        s = "\n"
        for r in range(len(self.grid)):
            s += str(self.grid[r])
            s += "\n"
        return s

    def is_currently_valid_col(self, col_index, current_row_index):
        correct_col_values = self.valid_cols[col_index]
        current_block_size = 0
        starting_index = 0
        next_starting_index = 0 
        for i in range(len(correct_col_values)):
            for j in range(starting_index, len(self.grid[0])):
                # Handles cases of 0s in the current cell
                if self.grid[j][col_index] == 0 and current_block_size != 0 and j < current_row_index: # Case 1: There is a 0 interrupting what should be a continuous block. Thus, the column is invalid and the method returns False.
                    return False
                if self.grid[j][col_index] == 0 and current_block_size == 0: # Case 2: There is a 0 but there is not a continuous block so it iterates to next index
                    continue
                
                # Handles cases of 1s in the current cell
                if self.grid[j][col_index] == 1 and current_block_size > correct_col_values[i]: # Case 1: There is a 1, making the block too long. Thus, the column is invalid and the method returns False.
                    return False
                if self.grid[j][col_index] == 1 and current_block_size < correct_col_values[i]: # Case 2: There is a 1 and the block isn't large enough yet, adds to the counter for block size.
                    current_block_size += 1
                    next_starting_index = j + 1
                
                # Checks if the current block is satisfied. Resets the block size counter and sets the starting index for the loop to the next index in the array.
                if current_block_size == correct_col_values[i]:
                    current_block_size = 0
                    starting_index = j+1
                    if starting_index >= len(self.grid[0]) and i == len(correct_col_values) - 1: # Checks if starting index is out of bounds and if we are checking the last block. If both are true then the column is valid and the method return True.
                        return True
                    elif starting_index >= len(self.grid[0]) and i < len(correct_col_values) - 1: # Checks if starting index is out of bounds and if there is a block remaining, if there is a block remaining then the column is invalid.
                        return False
                    elif self.grid[starting_index][col_index] == 1: # Since the if statement above failed, we check if the next index is a 1, if it is then the block is too long and the method return False.
                        return False
                    else: # If we hit this else statement, then we have another block to check and we break out of the inner loop to check the next block.
                        break
            starting_index = next_starting_index
        for j in range(starting_index, len(self.grid[0])): # Loops through the remaining indices checking if there is an extra block. Returns False if there is
            if self.grid[j][col_index] == 1:
                return False 
        if next_starting_index == 0  and current_row_index == self.grid_size - 1: # We are in the last row and the column is all zeros so method returns False
            return False
        return True

    def place_row(self, row_index, potential_row_index):
        row_to_try = self.potential_rows[row_index][potential_row_index]
        for i in range(len(self.grid[0])):
            self.grid[row_index][i] = row_to_try[i]
        return 0
    
    def clean_row(self, row_index):
        for i in range(len(self.grid)):
            self.grid[row_index][i] = 0
        return 0

    def find_valid_rows(self, row_index):
        correct_row_vals = self.valid_rows[row_index]
        potential_row = []
        min_num_cells = sum(correct_row_vals) + len(correct_row_vals) - 1
        for num_cells in correct_row_vals:
                potential_row += [1 for k in range(num_cells)]
                potential_row += [0]
        potential_row = potential_row[:-1]
        if min_num_cells == self.grid_size: # There is only one possible row for this row, creates the row and adds it to the dictionary of possible rows.
            self.potential_rows[row_index].append(potential_row)
            return self.potential_rows[row_index]
        else: # There are multiple possible rows; iterate through all possibilities and add them to the dictionary
            num_extra_zeros = self.grid_size - min_num_cells # Number of extra zeros needed to fill the remainder of the row
            gap_indices = [0] + [i for i, x in enumerate(potential_row) if x == 0] + [len(potential_row)-1] # Creates a list of indices where an extra zero can be placed
            # Using a triple-nested for loop, tries all possible amount of zeros in each gap by having effectively two pointers to try all placements of zeros 
            for num_zeros in range(1, num_extra_zeros+1):
                for gap1 in gap_indices[:-1]:
                    for gap2 in gap_indices[gap_indices.index(gap1)+1:]:
                        if gap2 != len(potential_row)-1:
                            current_potential_row = potential_row[:gap1] + [0 for k in range(num_zeros)] + potential_row[gap1:gap2] + [0 for k in range(num_extra_zeros - num_zeros)] + potential_row[gap2:]
                        else:
                            current_potential_row = potential_row[:gap1] + [0 for k in range(num_zeros)] + potential_row[gap1:] + [0 for k in range(num_extra_zeros -  num_zeros)]
                        
                        if current_potential_row not in self.potential_rows[row_index]: # Since there is potential for duplicate rows to show up, filters out rows already added to the dictionary
                            self.potential_rows[row_index].append(current_potential_row)
            current_potential_row = potential_row + [0 for k in range(num_extra_zeros)]
            if current_potential_row not in self.potential_rows[row_index]: # Handles edge case of adding all extra zeros to the end of the row
                self.potential_rows[row_index].append(current_potential_row)
            return self.potential_rows[row_index]
    
    def nonogram_solver_util(self, n):
        print("This is call number:", n)
        print(self)
        if n >= self.grid_size:
            return True
        for i in range(len(self.potential_rows[n])):
            self.place_row(n, i)
            row_works = True
            for c in range(len(self.grid[0])):
                if self.is_currently_valid_col(c, n) == False:
                    self.clean_row(n)
                    row_works = False
                    break
            
            if row_works == False:
                continue

            if self.nonogram_solver_util(n+1) == True:
                return True
            print("WE CLEANED A ROW")
            self.clean_row(n)

        return False

    def nonogram_solver(self):
        for i in range(self.grid_size):
            self.find_valid_rows(i)
        if self.nonogram_solver_util(0) == False:
            print("This Nonogram has no solution")
            return False
        else:
            print("The solution for this Nonogram is: \n", self)
            return True
        

def main():
    test_rows = [[3,5],[1,5],[1,6],[5],[2,4,1],[2,1],[3],[5,1],[1],[2,1,1]] # Array containing the correct number of "filled-in" squares for the rows of the grid
    test_cols = [[1,4,1],[3,4,1],[1,3],[1,1],[3,1],[5],[5,1],[4,1,1],[5,1],[3]] # Array containing the correct number of "filled-in" squares for the columns of the grid
    #test_rows = [[3,2],[1,1,1,1],[1,2,1,2],[1,2,1,1,3],[1,1,2,1],[2,3,1,2],[9,3],[2,3],[1,2],[1,1,1,1],[1,4,1],[1,2,2,2],[1,1,1,1,1,1,2],[2,1,1,2,1,1],[3,4,3,1]]
    #test_cols = [[4,3],[1,6,2],[1,2,2,1,1],[1,2,2,1,2],[3,2,3],[2,1,3],[1,1,1],[2,1,4,1],[1,1,1,1,2],[1,4,2],[1,1,2,1],[2,7,1],[2,1,1,2],[1,2,1],[3,3]]
    NonogramTest = Nonogram(10, test_rows, test_cols)
    NonogramTest.nonogram_solver()

main()