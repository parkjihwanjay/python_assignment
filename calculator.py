from module import *

print('Menu')
print('----')
print('1. add')
print('2. sub')
print('3. multiply')
print('4. divide')
print('5. stop')

select = input('선택 : ')

if select == '5':
    print('종료')
else:
    num1 = input('num1 : ')
    num1 = int(num1)
    num2 = input('num2 : ')
    num2 = int(num2)

    print('결과 : ', end='')

    if select ==  '1':    
         print(add(num1, num2))
    elif select == '2':
        print(sub(num1, num2))
    elif select == '3':
        print(multiply(num1, num2))
    elif select == '4':
        print(divide(num1, num2))

