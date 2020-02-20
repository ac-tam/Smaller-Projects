def listOfintegers(y, x):
    listY = []
    listX = []
    for i in range(y):
        listY.append(chessboard[i][x])
    for i in range(x):
        listX.append(chessboard[y][i])
    return list(set(listX + listY))

def findTheLowest(list):
    for i in range(list[-1] + 1):
        if list[i] != i:
            return i
    return i+1

chessboard = []
for i in range(int(input("How many rows?"))):
    chessboard.append([])

columns = int(input("How many columns?"))
for i in chessboard:
    for j in range(columns):
         i.append(-1)
for i in range(columns):
    chessboard[0][i] = i
for i in range(len(chessboard)):
    chessboard[i][0] = i

for y in range(len(chessboard)):
    for x in range(len(chessboard[0])):
        if chessboard[y][x] == -1:
            chessboard[y][x] = findTheLowest(listOfintegers(y,x))

print()
for i in chessboard:
    print(i)
