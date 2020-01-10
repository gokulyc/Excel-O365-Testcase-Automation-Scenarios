from math import sqrt
class sqroot():
    def getsqroot(self,num):
        return sqrt(num)

class addition():
    def getsum(self,a,b):
        return a+b

class subtraction():
    def getsub(self,a,b):
        return a-b

class multiplication():
    def getmul(self,a,b):
        return a*b

class division():
    def getdiv(self,a,b):
        return a/b

class mathnew(sqroot,addition,subtraction,multiplication,division):
        def callsupermethods(self):
            print(super().getsqroot(10))
            print(super().getsum(10,20))
            print(super().getsub(10,5))
            print(super().getmul(10,5))
            print(super().getdiv(10,5))

obj=mathnew()
obj.callsupermethods()
