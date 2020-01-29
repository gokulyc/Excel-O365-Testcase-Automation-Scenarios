import os
import re


def countvowel(word):
    count = 0
    for l in word.lower():
        if l in ['a', 'i', 'e', 'o', 'u']:
            count += 1
    return count

# print(countvowel('aeioucmskafjf'))

if __name__ == __name__:
    # print(os.getcwd())
    patterns = ['\w+']
    with open(r'1\sample.txt', mode='r') as myfile:  # modes r w a r+ w+
        contents = myfile.read()
        for pattern in patterns:
            words = re.findall(pattern, contents)
    countv = []
    for w in map(countvowel, words):
        countv.append(w)
    maxval = max(countv)
    for key,value in zip(words,countv):
        if value==maxval:
            print(key,':',value)
