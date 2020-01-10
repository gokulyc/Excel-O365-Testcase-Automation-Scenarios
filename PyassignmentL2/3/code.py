c = 0
def f2(x):
    # by adding below line
    global c
    c+= 1
    b = x + c
    print (c)
    return b
print (f2(1))
print (c )
