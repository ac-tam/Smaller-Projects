#Andrew Tam Binomial Theorem proof 4/7/20





#
# Manual

class term(object): #Represents a term such as 3x^2y^2
    def __init__(self, x, y, coefficient):
        self.coefficient = coefficient
        self.x = x #exponent of x term
        self.y = y #exponent of y term
    
    def __hash__(self): return self.x + 2* self.y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def multiply(self, other):
        return term(self.x + other.x,       #when you multiply by another term, add exponents
                    self.y + other.y,   
                    self.coefficient * other.coefficient) #multiply coefs

    
    def __str__(self):
        if self.x == 1 and self.y == 0:
            return ("{}x ".format(self.coefficient))
        if self.y == 1 and self.x == 0:
            return ("{}y ".format(self.coefficient))
        if self.x == 0:
            return ("{}y{} ".format(self.coefficient, self.y))
        if self.y == 0:
            return ("{}x{} ".format(self.coefficient, self.x))
       
        return ("{}x{}y{} ".format(self.coefficient, self.x, self.y))



class polynomial(object): #This object represents a polynomial
    def __init__(self, list_of_terms):
        self.terms = list_of_terms
        
    def multiply(self, other):  #multiply two polynomials by multiplying all terms against each other
        end_terms = []
        for this in self.terms:
            for oth in other.terms:
                end_terms.append(this.multiply(oth))
        return polynomial(end_terms)

    def combine_like_terms(self): #combine the like terms
        unique = []
        for i in self.terms:
            unique.append(term(i.x, i.y, 0))  #create a list of unique terms 
        unique = list(set(unique))


        for ter in self.terms:
            unique[ find(ter, unique) ].coefficient += ter.coefficient #increment the unique term 

        self.terms = list(unique)

    def __eq__(self, other):
        return self.terms == other.terms
    def __str__(self):
        stri =  ""
        for t in self.terms:
            stri += str(t) + "+ "
        return stri[:-2]

def find(a, arr): #simple search alg.
    for i in range(len(arr)):
        if arr[i] == a: return i
    


def expand_binomial_manually(x, y, power): #FOIL basicially
    result = [] 
    current = polynomial([x, y])
    binomial = polynomial([x, y])

    for i in range(power -1):
        current = current.multiply(binomial)
        current.combine_like_terms()
        if i != power -2:
            print("({}) * ({})".format(str(current), str(binomial))) #show your work
    return current


#
#   Binomial Theorem
#
def fact(n): #Factorial function
    prod = 1
    for i in range(1, n + 1): prod *= i
    return prod

def binomial_coefficient(n, k): #nCk

    return fact(n) / (fact(k)*(fact(n - k)))



def binomial_theorem(x, y, n):      #this implements the binomial theorem
    the_terms = []
    for i in range(n + 1):
        the_terms.append( 
                    term(   n - i , #x
                            i,      #y
                            int((x ** (n - i)) * (y ** i) * binomial_coefficient(n, i))  
                    ))
    return polynomial(the_terms)


#
#   Main "method"
#

def string_to_info(string): #take (ax+by)^n and separate the a b and n vals
    arr = [0, 0, 0]
    arr[0] = string[1:string.index("x")]
    arr[1] = string[string.index("+"):string.index("y")]
    arr[2] = string[string.index("^") + 1 :]
    for i in range(len(arr)):
        if arr[i] == ""  or arr[i] == "+" :
            arr[i] = 1
        else:
            arr[i] = int(arr[i])

    return arr


         
def main():
    print("This program will prove the binomial Theorem!\nInput the problem in the form (ax+by)^n.\nFor example, enter (2x+5y)^8")
    
    info = string_to_info(input("Input:"))
    print()
    term1 = term(1, 0, info[0])
    term2 = term(0, 1, info[1])

    manual = expand_binomial_manually(term1, term2, info[2])
    print()
    quick = binomial_theorem(info[0], info[1], info[2])
    print("Expand and combine like terms: {}".format(manual))
    print("Binomial Theorem:              {}".format(quick))
    if (manual == quick):
        print("It works!")
    else:
        print("Doesn't work")
    print()
    print()
    print()


while True: main()
