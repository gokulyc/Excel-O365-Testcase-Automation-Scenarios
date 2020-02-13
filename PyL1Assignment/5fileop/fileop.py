import os

print(os.getcwd())

output=''

with open(r'PyL1Assignment\5fileop\input.txt',mode='r') as myfile:
    contentline =myfile.readlines()
    i=0
    for line in contentline:
        i=i+1
        output=output+'number of characters,words per line '+str(i)+' :'+str(len(line))+','+str(len(line.split(' ')))+'\n'
    print(output)
    with open('output123.txt',mode='w') as target:
        target.write(output)
