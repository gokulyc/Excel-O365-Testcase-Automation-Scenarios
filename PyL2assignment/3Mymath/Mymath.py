from math import sqrt


class Mymath():

    def sqroot(self, num):
        return sqrt(num)

    def addition(self, num1, num2):
        '''
        num1+num2
        '''
        return num1+num2

    def subtraction(self, num1, num2):
        '''
        num1-num2
        '''
        return num1-num2

    def multiplication(self, num1, num2):
        '''
        num1*num2
        '''
        return num1*num2

    def division(self, num1, num2):
        '''
        num1/num2
        '''
        return num1/num2


if __name__ == "__main__":
    mobj = Mymath()

    num = float(input("Enter number to find square root :"))
    print(f"Square root of number {num} :", mobj.sqroot(num))
    num1 = float(input("Enter number1 :"))
    num2 = float(input("Enter number2 :"))
    print(f"Sum of {num1},{num2} :", mobj.addition(num1, num2))
    print(f"Subtraction of {num1},{num2} :", mobj.subtraction(num1, num2))
    print(f"Multiplication of {num1},{num2} :",
          mobj.multiplication(num1, num2))
    print(f"Division of {num1},{num2} :", mobj.division(num1, num2))
