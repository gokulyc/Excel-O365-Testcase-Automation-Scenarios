
class matrixadd():
    def __init__(self,A):
        self.A=A
        
    
    def __add__(self,B):
        a=self.A[0]+B[0]
        b=self.A[1]+B[1]
        c=self.A[2]+B[2]
        d=self.A[3]+B[3]
        return [a,b,c,d]

if __name__ == "__main__":
    A=[1,2,3,4]
    B=[5,6,7,8]

    obj=matrixadd(A)

    print(obj+B)
