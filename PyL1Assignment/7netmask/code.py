strnetmasklength = input('enter netmask length 8/16/32 :') 
netmasklength=int(strnetmasklength)

if netmasklength==8:
    print('netmask :','255.0.0.0')
    print('Class : A \n'+'No. of networks:','126')

elif netmasklength==16:
    print('netmask :','255.255.0.0')
    print('Class : B \n'+'No. of networks:','16,382')

elif netmasklength==24:
    print('netmask :','255.255.255.0')
    print('Class : C \n'+'No. of networks:','2,097,150')

else:
    print('wrong input')