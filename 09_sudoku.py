sudoku = []
all_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
output = "YES"

#Input and verify each row
for row in range(9):
    sudoku_row = input("Enter sudoku row: ")
    sudoku_row = list(sudoku_row)
    if sorted(sudoku_row) != all_digits:
        output = "NO"
        break
    sudoku.append(sudoku_row)

# Verify the columns if rows are valid
if output == "YES":
    for j in range(9):
        column = []
        for i in range(9):
          column.append(sudoku[i][j])
        if sorted(column) != all_digits:
            output = "NO"
            break

# Verify the sub-squares if columns are valid
if output == "YES":
    for m in range(3):
        n = 0
        for k in range(3):
            subsquare = []
            for i in range(3):
                for j in range(n, n + 3):
                    subsquare.append(sudoku[i][j])
            if sorted(subsquare) != all_digits:
                output = "NO"
                break
            n += 3
        if len(sudoku) > 3:
            sudoku = sudoku[3:]

#Result
print(output)
    
    


    
