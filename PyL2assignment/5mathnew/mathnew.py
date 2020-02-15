from Mymath import Mymath
# print(dir())
# print(Mymath)
# del(Mymath)
# import Mymath
# print(dir())
# print(Mymath)

class mathnew(Mymath):
    def __init__(self,sqnum,num1,num2):
        super().__init__(sqnum,num1,num2)

if __name__ == "__main__":

    num = float(input("Enter number to find square root :"))
    num1 = float(input("Enter number1 :"))
    num2 = float(input("Enter number2 :"))
    mobj = mathnew(num, num1, num2)
    print(f"Square root of number {num} :", mobj.sqroot())
    print(f"Sum of {num1},{num2} :", mobj.addition())
    print(f"Subtraction of {num1},{num2} :", mobj.subtraction())
    print(f"Multiplication of {num1},{num2} :",
          mobj.multiplication())
    print(f"Division of {num1},{num2} :", mobj.division())