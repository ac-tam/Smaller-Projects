def d(j, k):
    table = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
            [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
            [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
            [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
            [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
            [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
            [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
            [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
            ]
    return table[int(j)][int(k)]

def p(i, num):
    table = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
            [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
            [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
            [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
            [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
            [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
            [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]
        ]
    return table[int(i) % 8][int(num)]
def inv(i):
    return [0, 4, 3, 2, 1, 5, 6, 7, 8, 9][int(i)]


def verhoeffCheck(num):
    num = str(num)
    arr = [num[i] for i in range(len(num) -1, -1, -1)] #make the arr in reverse
    checkSum = 0 #check sum starts as 0
    for i in range(len(arr)):
        checkSum = d(checkSum, p(i, arr[i])) #Look at the tables
     return checkSum == 0 #verify
def verhoeffCreate(num):
    num = str(num)
    arr = [num[i] for i in range(len(num) -1, -1, -1)]#make the arr in reverse

    arr.insert(0, "0")#add an 0 at pos 0
    checkSum = 0 #check sum starts as 0
    for i in range(len(arr)):
        checkSum = d(checkSum, p(i, arr[i]))#Look at the tables
    return num + str(inv(checkSum))#find the checkdigit

print(verhoeffCreate(236))
