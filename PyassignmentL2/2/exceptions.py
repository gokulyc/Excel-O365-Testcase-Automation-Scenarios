
try:
    # print(a)
    # print(1/0)
    b=input('Enter any character :')
    print('a'+int(b))
except NameError:
    print('Name Error occured')
except KeyboardInterrupt:
    print('Keyboard Interrupt occured')
except ArithmeticError:
    print('Arithmetic Error')
else:
    print('Exception occured')
finally:
    print('In Finally block')