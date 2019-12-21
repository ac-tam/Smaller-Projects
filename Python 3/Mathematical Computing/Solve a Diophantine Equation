def gcf(a, b):
    r =  b % a
    while r != 0:

        r = b % a
        b = a
        if r != 0:
            a = r
    return a

def isInt(a):
    return int(a) == a

def solveDiophantine(A, B, D): #Ax + By = D
    if D % gcf(A, B) == 0:
        if A > B:
            for x in range(B + 1):
                if isInt((D - A*x)/B): #this thing is the y
                    print("The solutions to the equation are: ")
                    print("x = " + str(x) + " + " + str(B) + "t")
                    print("y = " + str((D - A*x)/B) + " - " + str(A) + "t")
                    break
        else: #makes it more efficient
            for y in range(A + 1):
                if isInt((D - B * y) / A):  # this thing is the x
                   print("The solutions to the equation are: ")
                   print("x = " + str((D - B * y) / A) + " + " + str(B) + "t")
                   print("y = " + str(y) + " - " + str(A) + "t")
                   break
    else:
        print("The GCF does not divide the D, so there are no integer solutions!")
