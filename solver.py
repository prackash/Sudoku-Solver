
#This function takes in the board as a parameter and returns the solved sudoku board 
def solve(bo):
    find = find_empty(bo)   #Identifies the zero value in the board and stores the rows and cols if it exists
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

#This function takes in the parameters board , pos (row and column) and the integer that is to be placed in that pos and returns if the conditions are met or not
def valid(bo, pos, num):
    

    # Check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Col
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False

    # Check box

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

#This Function takes in the parameter board and finds the empty spaces (0) in the board and returns the row and col of that cell 
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None

#This function takes in the parametere board and prints the board in a proper format and does not return any value
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(bo[i][j],end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")

#Enter the board values as list of lists 
board=[[0,0,0,0,0,0,6,8,0],[0,0,0,0,7,3,0,0,9],[3,0,9,0,0,0,0,4,5],[4,9,0,0,0,0,0,0,0],[8,0,3,0,5,0,9,0,2],[0,0,0,0,0,0,0,3,6],[9,6,0,0,0,0,3,0,8],[7,0,0,6,8,0,0,0,0],[0,2,8,0,0,0,0,0,0]]
solve(board)
print_board(board)
