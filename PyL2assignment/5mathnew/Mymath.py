from math import sqrt


class Mymath():

    def __init__(self, sqnum, num1, num2):
        '''
        sqnum for finding sqroot of number
        num1,num2 for finding addition,subtraction,multiplication,division
        '''
        self.sqnum = sqnum
        self.num1 = num1
        self.num2 = num2

    def sqroot(self):
        return sqrt(self.sqnum)

    def addition(self):
        '''
        num1+num2
        '''
        return self.num1+self.num2

    def subtraction(self):
        '''
        num1-num2
        '''
        return self.num1-self.num2

    def multiplication(self):
        '''
        num1*num2
        '''
        return self.num1*self.num2

    def division(self):
        '''
        num1/num2
        '''
        return self.num1/self.num2


if __name__ == "__main__":

    num = float(input("Enter number to find square root :"))
    num1 = float(input("Enter number1 :"))
    num2 = float(input("Enter number2 :"))
    mobj = Mymath(num, num1, num2)
    print(f"Square root of number {num} :", mobj.sqroot())
    print(f"Sum of {num1},{num2} :", mobj.addition())
    print(f"Subtraction of {num1},{num2} :", mobj.subtraction())
    print(f"Multiplication of {num1},{num2} :",
          mobj.multiplication())
    print(f"Division of {num1},{num2} :", mobj.division())
