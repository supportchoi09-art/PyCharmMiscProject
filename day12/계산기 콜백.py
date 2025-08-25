'''
실행함수
x,y를 받음 (operation으로) //
연산자를 행동함수로 만들어줄 함수 필요

행동함수
더하기 함수
마이너스함수
곱하기 함수
나누기(몫)함수
'''

'''
def plus (x, y):
    print(x + y)

def minus(x, y):
    print(x - y)

def multiply(x, y):
    print(x * y)

def divide(x, y):
    print(x / y)

def operation(op,x,y):
    op(x,y)

operation(plus,3,4)
operation(minus,7,4)
operation(multiply,8,4)
operation(divide,9,3)
'''


def calculator(x,y,operation):
    return operation(x,y)

def plus(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

plus_result = calculator(2,3,plus)
print(plus_result)

plus_result = calculator(7,3,minus)
print(plus_result)

plus_result = calculator(2,3,multiply)
print(plus_result)

plus_result = calculator(9,3,divide)
print(plus_result)

