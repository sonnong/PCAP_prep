def DisplayBoard(board):
    for row in board:
        print("+-------+-------+-------+\n|       |       |       |")
        print("|  ", row[0], "  |  ", row[1], "  |  ", row[2], "  |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def EnterMove(board):
    user_move = int(input("Enter your move: "))
    for row in board:
        for i in range(3):
            if row[i] == user_move:
                row[i] = "O"

def MakeListOfFreeFields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                free_fields.append((i, j))
    return free_fields
        

def VictoryFor(board, sign):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign or board[0][i] == board[1][i] == board[2][i] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] ==  sign or board[0][2] == board[1][1] == board[0][2] == sign:
        return True
    return False
        
from random import randrange
def DrawMove(board):
    free_fields = MakeListOfFreeFields(board)
    computer_move = free_fields[randrange(len(free_fields))]
    board[computer_move[0]][computer_move[1]] = "X"

#initializing the board
board = [[1,2,3],
         [4, "X", 6],
         [7, 8, 9]]
DisplayBoard(board)
print("Computer moved. Your turn now.")
while True:
    EnterMove(board)
    DisplayBoard(board)
    if VictoryFor(board, "O") == True:
        print("You have won.")
        break
    DrawMove(board)
    DisplayBoard(board)
    if VictoryFor(board, "X") == True:
        print("Computer has won.")
        break
