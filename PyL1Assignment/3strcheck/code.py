# str1=input("Enter a string : ")


def checkchar_e(str1):
    count=0
    for ch in str1.lower():
        if ch == 'e':
            count=count+1
    if count>=2 :
        return True
    else:
        return False

if __name__ == "__main__":
    str1=input("Enter a string : ")
    print('Is string contain 2 e\'s :',checkchar_e(str1))  