#At each input, input a connecting vertex followed by the weight E.G. Vertex 0 connects to 1 and 2 with weights 1 and 2 respectively, enter 1,1,2,2
def createGraph(num):
    matrix = []
    for i in range(num):
        matrix.append([])
        for j in range(num):
            matrix[i].append(0)
    for i in range(num):
        arr = input(i).split(",")
        for n in range(len(arr)):
            arr[n] = int(arr[n])
        for j in range(0, len(arr),2):
            matrix[i][arr[j]] = arr[j + 1]
            matrix[arr[j]][i] = arr[j + 1]
    return matrix
