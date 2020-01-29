import os
import re
import pandas as pd
import numpy as np

# print(os.getcwd())
# print(pd,dir(pd))


def GetStudentUniqueIDs():
    li=getfiletolist()
    idset=set()
    llen=li.__len__()
    i=4
    while(i!=llen):
        idset.add(li[i])
        i=i+4
    return idset

def printstudentdetails(id):
    df = pd.read_csv('student.txt')
    df.columns=[column.replace("<", "") for column in df.columns] 
    df.columns=[column.replace(">", "") for column in df.columns] 
    # print(df)
    str1=f'Rollno=={id}'
    student1=df.query(str1,inplace=False)
    # print(student1)
    r,c=student1.shape
    out=''
    for i in range(r):
        t1=student1.iloc[[i],[0]].values[0][0]
        # print(t1)
        t2=student1.iloc[[i],[1]].values[0][0]
        t3=student1.iloc[[i],[2]].values[0][0]
        t4=student1.iloc[[i],[3]].values[0][0]
        out+=getstr_template(t1,t2,t3,t4)+'\n' 
    # print(out)
    total_marks=student1.sum().values[3]
    out=out+'\t\tTotal : '+str(total_marks)
    # print(out)
    return out,student1.iloc[[i],[1]].values[0][0],student1.iloc[[i],[0]].values[0][0]


# Read Student Data
def getfiletolist():
    patterns=[r'\w+']
    with open('student.txt',mode='r') as myfile1:
        contents=myfile1.read()
        # print(contents)
    for pattern in patterns:
        # print(f'Searching for the phrase using the re check :{pattern}')
        extractlist=re.findall(pattern,contents)
        # print(extractlist,'\n')
        return extractlist

def getstr_template(a,b,c,d):
    '''
    {Id:<Rollno>, Name:<StudName>,subject:<Subject>,marks:<Marks>}
    strings in <[name]> are replaced in template from file
    '''
    
    with open('tempstud.txt',mode='r') as myfile1:
        contents=myfile1.read()
    # print(contents)
    contents=contents.replace('<Rollno>',str(a))
    contents=contents.replace('<StudName>',str(b))
    contents=contents.replace('<Subject>',str(c))
    contents=contents.replace('<Marks>',str(d))
    # print(contents)
    return contents


if __name__ == "__main__":
    # print(getfiletolist())
    # print(GetStudentUniqueIDs())
    for i in GetStudentUniqueIDs():
        print(printstudentdetails(i)[0])
        nameoffile=str(printstudentdetails(i)[1])+'.'+str(printstudentdetails(i)[2])+'.txt'
        with open(nameoffile,mode='w') as myfile1:
            myfile1.write(printstudentdetails(i)[0])
    # getstr_template(1,2,3,4)