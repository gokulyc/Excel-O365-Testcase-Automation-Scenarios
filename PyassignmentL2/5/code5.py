import os,re
os.getcwd()
patterns=['\w*[aeiou][aeiou]\w*']
with open('info.txt',mode='r') as myfile:
    contents=myfile.read()
    print(contents)

for pattern in patterns:
        print(f'Searching for the phrase using the re check :{pattern}')
        print(re.findall(pattern,contents),'\n')