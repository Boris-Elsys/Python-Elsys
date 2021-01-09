board = [[" "," "," "], [" "," "," "],[" "," "," "]]

def printBoard(board):
    print("  1  2  3")
    for x in range(3):
        for y in range(3):
            if y == 0:
                print(x + 1, end = "")
        print("\n")

def win(board):
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2] != " ":
            return True

    for y in range(3):
        if board[0][y] == board[1][y] == board[2][y] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    elif board[2][0] == board[1][1] == board[0][2]:
        return True

    return False
    
def free(x, y, board):
    print(board[x][y])
    if board[x][y] != " ":
        return False

    return True
    
cords = [0,0]

for i in range(9):
    printBoard(board)
    n = i % 2
    print("player{", n + 1, "}s turn:")
    while True:
        cords[0] = int(input("x position: "))-1
        cords[1] = int(input("y position: "))-1
        if free(cords[0], cords[1], board):
            break
            
        print("bad entry")
        
    if (i % 2) == 0:
        board[cords[0]][cords[1]] = "O"
    else:
        board[cords[0]][cords[1]] = "X"

    if i >= 4:
        if win(board):
            printBoard(board)
            print("player{", n + 1, "} wins")
            break
