class rev_iter():
    def __init__(self):
        pass

    def getrev(self,iterobj):
        try:
            li=[]
            l=len(iterobj)
            for item in range(l):
                li.append(iterobj[l-item-1])
            return li
        except TypeError:
            print('TypeError Occured')

obj1=rev_iter()
print(obj1.getrev('abcdefg'))
print(obj1.getrev(['q','w','e','r','t','y']))
print(obj1.getrev(10))









