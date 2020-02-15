

class StrGrt():
    def __init__(self,str1):
        self.str1=str1

    def __gt__(self,str2):
        l1=len(self.str1)
        l2=len(str2)
        if l1>l2:
            return True
        else:
            return False

if __name__ == "__main__":
    str1=input('Enter 1st string :')
    str2=input('Enter 2nd string :')

    strobj=StrGrt(str1)
    print(f'Is string {str1} > {str2} : ',strobj>str2)
