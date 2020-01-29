def binomialCoeff(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1)   
    return res 

def printPascal(n) : 
      
    # Iterate through every line  
    # and print entries in it 
    for line in range(0, n) : 
        print(' ')  
        # Every line has number of  
        # integers equal to line 
        # number 
        for i in range(0, line + 1) : 
            print(binomialCoeff(line, i), 
                " ", end = "") 
        print() 

n = 7
printPascal(n) 
# print(binomialCoeff(10, 5))