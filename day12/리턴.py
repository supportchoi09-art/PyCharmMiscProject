def plus(a,b):
    return a+b

sum = plus(10,20)
print(sum)

print(plus(10,20))

def multiyply(num):
    result = num*7
    return result # result 에 있는 숫자를 넘긴다는 뜻

print(multiyply(3)) #계산한 값을 넘긴다

def bools_check():
    return True

print(bools_check())


#어떤 값을 넘겼을때 리턴과 매개변수를 사용해서 7의 배수인지 아닌지 판단해주는 함수 만들기
#True / False로 맞는지 아닌지 판단하기

def ply(num2):
    result = num2%7
    return True if result == 0 else False
print(ply(14))
print(ply(15))


def check(num):
    if num % 7 == 0:
        return True
    else:
        return False

print(check(14))
