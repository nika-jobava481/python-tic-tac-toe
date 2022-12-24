board = [["_" for _ in range(3)] for _ in range(3)]

char="X"
counter=0

def printBoard():
    for i in range(3):
        print(board[i])

def isEmpty():
    status = False
    for i in range(3):
        for j in range(3):
            if board[i][j]=="_":
                status=True
                return status
    return status

def checkBoard():
    if board[0][0]==board[0][1] and board[0][1] == board[0][2] and board[0][2]!="_" or board[1][0]==board[1][1] and board[1][1] == board[1][2] and board[1][2]!="_" or board[2][0]==board[2][1] and board[2][1] == board[2][2] and board[2][2]!="_" or board[0][0]==board[1][0] and board[1][0] == board[2][0] and board[2][0]!= "_" or board[0][1]==board[1][1] and board[1][1] == board[2][1] and board[2][1]!= "_" or board[0][1]==board[1][1] and board[1][1] == board[2][1] and board[2][1]!= "_" or board[0][0]==board[1][1] and board[1][1] == board[2][2] and board[2][2]!= "_" or board[0][2]==board[1][1] and board[1][1] == board[2][0] and board[2][0]!= "_":
        return True
    return False

def isEmptySpot(ch):
    return ch=="_"

while isEmpty():
    if checkBoard():
        print("Winner is  " + char)
        break
    printBoard()
    x=int(input("input row: "))
    y=int(input("input column: "))
    if isEmptySpot(board[x][y]):
        char="X"
        if counter%2==1:
            char="O"
        board[x][y]=char
        counter+=1
    else:
        print("input x and y for empty spot")
else:
    print("Draw!")