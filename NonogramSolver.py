from itertools import permutations

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
        if next_starting_index == 0  and current_row_index == self.grid_size - 1 and correct_col_values != [0]: # We are in the last row and the column is all zeros so method returns False
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
    
    def is_valid_row(self, row_index, potential_row):
        correct_row_values = self.valid_rows[row_index]
        current_block_size = 0
        starting_index = 0
        for i in range(len(correct_row_values)):
            for j in range(starting_index, len(self.grid)):
                # Handles cases of 0s in the current cell
                if potential_row[j] == 0 and current_block_size != 0: # Case 1: There is a 0 interrupting what should be a continuous block. Thus, the row is invalid and the method returns False.
                    return False
                if potential_row[j] == 0 and current_block_size == 0: # Case 2: There is a 0 but there is not a continuous block so it iterates to next index
                    continue

                # Handles cases of 1s in the current cell
                if potential_row[j] == 1 and current_block_size > correct_row_values[i]: # Case 1: There is a 1, making the block too long. Thus, the row is invalid and the method returns False.
                    return False
                if potential_row[j] == 1 and current_block_size < correct_row_values[i]: # Case 2: There is a 1 and the block isn't large enough yet, adds to the counter for block size.
                    current_block_size += 1

                # Checks if the current block is satisfied. Resets the block size counter and sets the starting index for the loop to the next index in the array.
                if current_block_size == correct_row_values[i]:
                    current_block_size = 0
                    starting_index = j+1
                    if starting_index >= len(self.grid) and i == len(correct_row_values) - 1: # Checks if starting index is out of bounds and if we are checking the last block. If both are true then the row is valid and the method return True.
                        return True
                    elif potential_row[starting_index] == 1: # Since the if statement above failed, we check if the next index is a 1, if it is then the block is too long and the method return False.
                        return False
                    else: # If we hit this else statement, then we have another block to check and we break out of the inner loop to check the next block.
                        break

        if 1 in potential_row[starting_index:]:
            return False # If there is another 1 found passed the loop, then there is an extra block and the method returns False.
        else:
            return True # If we finished iterating through all of the row values and indices in the row then the row is valid and the method returns True.
    
    def find_valid_rows(self, row_index):
        correct_row_vals = self.valid_rows[row_index]
        potential_row = []
        min_num_cells = sum(correct_row_vals) + len(correct_row_vals) - 1
        if correct_row_vals == [0]:
            potential_row = [0 for k in range(self.grid_size)]
            self.potential_rows[row_index].append(potential_row)
            return self.potential_rows[row_index]
        if min_num_cells == self.grid_size: # There is only one possible row for this row, creates the row and adds it to the dictionary of possible rows.
            for num_cells in correct_row_vals:
                potential_row += [1 for k in range(num_cells)]
                potential_row += [0]
            potential_row = potential_row[:-1]
            self.potential_rows[row_index].append(potential_row)
            return self.potential_rows[row_index]
        else: # There are multiple possible rows; iterate through all possibilities and add them to the dictionary
            row_elements = []
            num_extra_zeros = self.grid_size - min_num_cells
            for i in range(len(correct_row_vals)):
                potential_row = [1 for k in range(correct_row_vals[i])]
                if i != len(correct_row_vals) - 1:
                    potential_row += [0]
                row_elements.append(potential_row)
            for z in range(num_extra_zeros):
                row_elements.append([0])
            all_permutations = permutations(row_elements)
            checked_permutations = {}
            checked_permutations[0] = []
            for tup in all_permutations:
                if tup in checked_permutations[0]:
                    continue
                checked_permutations[0].append(tup)
                row = list(tup)
                row = [block for sublist in row for block in sublist]
                if self.is_valid_row(row_index, row) == True and row not in self.potential_rows[row_index]:
                    self.potential_rows[row_index].append(row)
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
            print("Finding valid rows for row", i)
            self.find_valid_rows(i)
        if self.nonogram_solver_util(0) == False:
            print("This Nonogram has no solution")
            return False
        else:
            print("The solution for this Nonogram is: \n", self)
            return True
        
def main():
    test_rows = [[3,5],[1,5],[1,6],[5],[2,4,1],[2,1],[3],[5,1],[1],[2,1,1]] # Working Case
    test_cols = [[1,4,1],[3,4,1],[1,3],[1,1],[3,1],[5],[5,1],[4,1,1],[5,1],[3]] # Working Case
    # Case Fails: Takes forever
    #test_rows = [[3,2],[1,1,1,1],[1,2,1,2],[1,2,1,1,3],[1,1,2,1],[2,3,1,2],[9,3],[2,3],[1,2],[1,1,1,1],[1,4,1],[1,2,2,2],[1,1,1,1,1,1,2],[2,1,1,2,1,1],[3,4,3,1]]
    # Case Fails: Takes forever
    #test_cols = [[4,3],[1,6,2],[1,2,2,1,1],[1,2,2,1,2],[3,2,3],[2,1,3],[1,1,1],[2,1,4,1],[1,1,1,1,2],[1,4,2],[1,1,2,1],[2,7,1],[2,1,1,2],[1,2,1],[3,3]]
    #test_rows = [[2],[4],[6],[8],[10],[4,4],[4,4],[10],[10],[10]]
    #test_cols = [[6],[7],[8],[9],[5,3],[5,3],[9],[8],[7],[6]]
    NonogramTest = Nonogram(10, test_rows, test_cols)
    NonogramTest.nonogram_solver()

main()