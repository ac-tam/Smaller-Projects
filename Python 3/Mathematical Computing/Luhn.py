def verify(barcode):
    evenSum = 0
    oddSum = 0
    for i in range(0, len(barcode) - 1, 2):
        oddSum += int(barcode[i]) #sum up odd pos
        evenSum += int(barcode[i + 1])#sum up even pos
    oddSum *= 3 #multiply the odd sum by 3

    theSum = oddSum + evenSum # add them

    theSum  = theSum % 10 #the total sum mod 10
    return 10 - theSum == int(barcode[-1]) #compare

print(verify("6523721664831"))
