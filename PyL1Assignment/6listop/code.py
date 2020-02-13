list1 =[x for x in range(3) ]
list2 =[x for x in range(3,6) ]
list3 =[x for x in range(6,9) ]



def maxlist(lst):
    m1=max(lst)
    lst.remove(m1)
    m2=max(lst)
    return [m1,m2]

def minlist(lst):
    m1=min(lst)
    lst.remove(m1)
    m2=min(lst)
    return [m1,m2]
# print(list1,list2,list3)

def getavg(lst):
    n=len(lst)
    lsum=sum(lst)
    return lsum/n





maxlst=[]
minlst=[]
maxlst.extend(maxlist(list1))
maxlst.extend(maxlist(list2))
maxlst.extend(maxlist(list3))
minlst.extend(minlist(list1))
minlst.extend(minlist(list2))
minlst.extend(minlist(list3))
print('Maximum list :',maxlst)
print('Average of Maximum list :',getavg(maxlst))
print('Minimum list :',minlst)
print('Average of Minimum list :',getavg(minlst))