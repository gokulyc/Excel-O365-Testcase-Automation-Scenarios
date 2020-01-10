import re 

patterns=['\d[a-zA-Z]+\d','\s\w+','\S+']

phrase='2fdfd4 ddgfb3 5vcbsfb'

for pattern in patterns:
        print(f'Searching for the phrase using the re check :{pattern}')
        print(re.findall(pattern,phrase),'\n')