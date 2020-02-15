import math


def sqroot(num):
    return math.sqrt(num)


def addition(num1, num2):
    '''
    num1+num2
    '''
    return num1+num2


def subtraction(num1, num2):
    '''
    num1-num2
    '''
    return num1-num2


def multiplication(num1, num2):
    '''
    num1*num2
    '''
    return num1*num2


def division(num1, num2):
    '''
    num1/num2
    '''
    return num1/num2


if __name__ == "__main__":
    num = float(input("Enter number to find square root :"))
    print(f"Square root of number {num} :", sqroot(num))
    num1 = float(input("Enter number1 :"))
    num2 = float(input("Enter number2 :"))
    print(f"Sum of {num1},{num2} :", addition(num1, num2))
    print(f"Subtraction of {num1},{num2} :", subtraction(num1, num2))
    print(f"Multiplication of {num1},{num2} :", multiplication(num1, num2))
    print(f"Division of {num1},{num2} :", division(num1, num2))
