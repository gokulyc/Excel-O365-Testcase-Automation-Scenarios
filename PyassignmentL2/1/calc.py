
def factorial(n):
    res=1
    while n != 1:
        res=res*n
        n=n-1
    return res

from math import log10
def findlog10(num):
    return(log10(num))

from math import radians,degrees
def toRadians(num):
    return radians(num)

from math import sin,cos,tan,pi

def getsin(v_radian):
    return sin(v_radian)

def getcos(v_radian):
    return cos(v_radian)

def gettan(v_radian):
    return tan(v_radian)


if __name__ == "__main__":
    n=input('Enter interger to find factorial : ')
    print(factorial(int(n)))

    n1=input('Enter num to find log 10 is ')
    print('log10 of {} : {}'.format(n1,log10(float(n1))))

    n2=input('Enter number to convert to radians :')
    print('{} coverted into Radians is {}'.format(n2,toRadians(float(n2))))

    

    