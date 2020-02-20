def columnSwap(arr, i, i2): 
  indexone = arr[i]
  arr[i] = arr[i2]
  arr[i2] = indexone

def printMatrix(matrix):
  print()
  for i in range(len(matrix)):
      print(matrix[i])

def rowSwap(arr, i, i2):
  for h in range(len(arr)):
    one = (arr[h])[i]
    (arr[h])[i] = (arr[h])[i2]
    (arr[h])[i2] = one

def makeMatrix(rowLength):
  returnThis = []
  anotherList = []
  theList = 0;
  for i in range(rowLength):
    theList = input("Row" + str(i) +": ")
    anotherList = []
    for e in range(rowLength):
      anotherList.append(theList[e])
    returnThis.append(anotherList)
  return returnThis

def iso(arr, arr2):
  temp = 0
  for a in range(len(arr)):
    for b in range(len(arr2)):
      rowSwap(arr, a, b)
      if arr == arr2:
        temp =+ 1
        print("They are isomorphic")
        

  for a in range(len(arr)):
    for b in range(len(arr)):
      columnSwap(arr, a, b)
    if arr == arr2:
      temp =+ 1
      print("They are isomorphic")

  for a in range(len(arr)):
    for b in range((len(arr2))):
      rowSwap(arr, a, b)
      columnSwap(arr, a , b)
      if arr == arr2:
        temp =+ 1
        print("They are isomorphic")

  if (temp == 0):
    print('The graphs are not isomorphic')

graph1 = makeMatrix(int(input("How big? ")))
graph2 = makeMatrix(int(input("How big? ")))
iso(graph1, graph2)
