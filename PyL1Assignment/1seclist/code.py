mylist = range(4)
print(type(mylist))
seclist = mylist
print(seclist)
# mylist.append(4)
print(seclist)
seclist = mylist[:]
print(seclist)
mylist.append(5)
print(seclist)


# mylist,range is generator object hence the error 
# range is inbuit generator