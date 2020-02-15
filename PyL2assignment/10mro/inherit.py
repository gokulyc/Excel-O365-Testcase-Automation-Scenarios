
class First():
    def method1(self):
        print("In Class 1",self)

class Second(First):
    def method1(self):
        print("In Class 2",self)

class Third(First):
    def method1(self):
        print("In Class 3",self)

class Fourth(Second,Third):

    pass
    # def method1(self):
    #     print("In Class 4",self)

if __name__ == '__main__':
    obj1=First()

    obj1.method1()

    obj2=Second()

    obj2.method1()

    obj3=Third()

    obj3.method1()

    obj4=Fourth()

    obj4.method1()

    print(Fourth.__mro__)


