import math
def isPrime(numm):
    for i in range(2, int(math.sqrt(numm)) + 1):
        if numm % i == 0:
            return False
    return True

def isPerfectSquare(myNum):
    return int((myNum ** 0.5)) == myNum ** 0.5
while True:
    print()
    num = int(input("Enter a number: "))
    factors = [1]

    if isPerfectSquare(num):
        if not (isPrime(num)):
            for i in range(2, int(math.sqrt(num)) + 1):

                if num % i == 0:
                    factors.append(i)

            for n in range(len(factors) - 2, 0, -1):
                factors.append(int(num / factors[n]))
    else:
        if not (isPrime(num)):
            for i in range(2, int(math.sqrt(num)) + 1):

                if num % i == 0:
                    factors.append(i)

            for n in range(len(factors) - 1, 0, -1):
                factors.append(int(num / factors[n]))

    factors.append(num)
    print("Factors of", num, "are", factors)
    print("There are", len(factors), "factors in", num)

    if(isPerfectSquare(num)):
        print(str(num), "is a perfect square!")
    if (len(factors)== 2):
        print(str(num), "is prime!")
    sod = 0
    for n in factors:
        sod += n

    print("The sum of the divisors is", sod)

    # Find prime factorization
    current = num
    pF = []

    for i in range(2,num+1):
        if isPrime(i):
            while (current / i == int(current / i)):
                current = current / i
                pF.append(i)
    pFordered = []
    count = 1
    pF.append(0)
    for i in range(len(pF)-1):
        if pF[i] == pF[i+1]:
          count += 1
        else:
            pFordered.append([pF[i], count])
            count = 1
    primeFactor = "The prime factorization of " + str(num) + " is "
    for i in pFordered:
         primeFactor += str(i[0])
         primeFactor +=  "^"
         primeFactor += str(i[1])
         if(not(i== pFordered[-1])):
            primeFactor += " * "
    print(primeFactor)

