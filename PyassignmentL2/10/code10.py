import time

def getexectime(original_func):
    def wrap_func():
        t1=time.time()
        original_func()
        time.sleep(1)
        t2=time.time()
        print('Execution time of {} is {}'.format(original_func,t2-t1))
    return wrap_func


@getexectime
def func_need_decorator():
    print("I want to be decorated!!")
    
@getexectime
def sumofsquares():
    sum=0
    for item in range(1000):
        sum=sum+(item*item)
    print(sum)


func_need_decorator()
print(sumofsquares())