def fibo(num):
    a=0
    b=1
    for num in range(num):
        sum=a+b
        yield sum
        a,b=b,sum

for k,num1 in enumerate(fibo(10)):
    print(k,num1)