'''
1. 에러 (우리가 잘못 입력한 것) ex) print(7/0)
2. 예외 (사용자의 입력 오류에 따라 발생) --> 우리가 예상하지 못한다.

'''
'''
num1 = int(input("첫번재 정수를 입력하세요 : "))
num2 = int(input("두 번째 정수를 입력하세요. : "))
if num2 == 0:
    print("0을 제외한 정수를 입력해주세요.")
else:
    print(f"{num1} / {num2} 의 결과는 : {num1/num2} 입니다. ")
# 첫번재 정수는 잘 넣었는데, 두번째 정수를 0을 넣으면 애러가 발생한다. (이 상황은 '예외'라고 한다) / 사용자가 0을 넣을것이라 상상하지 못한 것
'''
'''
BaseExceprion : 최상위 예외클래스 (모든 예외를 포용하는 애) 
Exception : 최상위보다 한단계 낮은것 (대부분의 예외를 감쌀 수 있다) // 대부분 예외클래스의 슈퍼클래스 (거의 모든 예외클래스가 이 클래스의 자식)
ArithmeticError : 산술연산오류
     OverflowError : 결과가 너무 커서 표현할 수 없음
     zeroDivisionError : 0으로 나누려고 할 때 발생
     FloationPointError : 실수연산에서 오류
AttributeError : 잘못된 속성 참조 (뭔가 없는걸 있다고 했을때?)
EOFError : 파일에서 더이상 읽을 데이터가 없을때 (파일을 다봤고 더 볼 게 없을때 뜨는 에러)
Module NotFoundError : import할 모듈이 없을때 (import를 해야겠다고 했는데, 모듈이 없을때)
FileFoundError : 존재하지 않는 파일을 찾으려고 할 때
IndexError : 잘못된 인덱스를 사용 (3개 인덱스밖에 없는데 4개를 물어볼때 등등)
NameError : 변수를 선언하지 않고 사용할때
SyntaxError : 코드 문법을 어기면 나온다. 
TypeError : 서로 다른 데이터 타입끼리 연산하려고 하면 발생한다. (문자열이랑 숫자열을 이것저것 연산하려고 하면 발생하게 된다.)
ValueError : 계산하려는 데이터값 오류!
'''



try:
    num1 = int(input("첫번재 정수를 입력하세요 : "))
    num2 = int(input("두 번째 정수를 입력하세요. : "))
    print(f"{num1} / {num2} 의 결과는 : {num1/num2} 입니다. ")
except ArithmeticError:
    print("산술 연산 예외발생") #오류가 발생할 것 같을때 출력되는 것들 (어떤일이 발생해도 에러메세지가 뜨지 않는다.)
# try / except로는 모든 예외상황을 완벽하게 처리하지 못한다.
except ValueError:
    print("입력값을 확인하세요. 예외발생 ")
#아! 뭔가 입력값(데이터값)이 잘못되었구나! ==> 에러 클래스를 써주게 되면 예외에 따라서 구체적으로 에러가 뭔지 구별할 수 있게 된다.

try:
    list = [1,2,3,4]
    print(list[5])
except IndexError:
    print("인덱스 범위를 벗어났습니다.")