class First():
    def Method1(self):
        print('In Class First')

class Second(First):
    def Method1(self):
        print('In Class Second')

class Third(First):
    def Method1(self):
        print('In Class Third')

class Fourth(Second,Third):
    pass
    # def Method1(self):
    #     print('In Class Fourth')
    
obj=Fourth()
obj.Method1()
print(Fourth.mro())

