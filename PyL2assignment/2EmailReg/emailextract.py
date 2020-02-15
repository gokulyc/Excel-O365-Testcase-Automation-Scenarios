email='From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016'

import re

patterns=['[a-zA-Z]+.[a-zA-Z]+@[a-zA-Z]+.com','[a-zA-Z]+.com',r'\d+:\d+:\d+']

# phrase='2fdfd4 ddgfb3 5vcbsfb'
li=[]

for pattern in patterns:
        # print(f'Searching for the phrase using the re check :{pattern}')
        li.extend(re.findall(pattern,email))
        # print(re.findall(pattern,email),'\n')
# print(li)

if __name__ == '__main__':
    print('Email : ',li[0])
    print('domain name : ',li[1])
    print('Time : ',li[2])