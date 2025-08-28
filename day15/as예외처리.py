'''
try:
    num1 = int(input("첫번째 정수를 입력 :  "))
    num2 = int(input("두번째 정수를 입력 : "))
    print(f"{num1} 나누기 {num2}의 결과는 {num1/num2}입니다.")

except ArithmeticError as e:
    print(f"산술 연산 예외발생! 상세 메세지는 {e}입니다.")
    # 무슨 에러인지 type도 알려주게 된다. (예외에 대한 자세한 정보도 가져올 수 있게 된다)
   '''
try:
    list = [1,2,3,4]
    print(list[5])
    print("try 구문 안에 예외발생 후 실행할 코드")
except IndexError as e:
    print(e)
finally:
    print("try 구문 안에 예외발생 후 실행할 코드")

print("try-except 구문 밖 코드 ")


try:
    number = int(input("좋아하는 숫자를 입력해주세요 : "))
except ValueError as error:
    print(error)
 #여기는 에러 메세지를 출력해주는 것이다. (except구문)
else:
    if number % 2 == 0:
        print("님이 좋아하는 숫자는 짝수~")
    elif number < 0:
        print("음수를 좋아하시는군요")
    else:
        print("홀수를 좋아하시는군요!")
