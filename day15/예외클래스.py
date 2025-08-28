#age = int(input("나이를 입력해주세요 : "))
#print(f"저의 나이는 {age}살 입니다. ") #현실세계에서는 음수인 나이는 없기 떄문에 예외 처리를 해줘야한다.

#raise를 사용해서 현실세계의 예외 처리를 해줘야한다.

try:
    age = int(input("나이를 입력해주세요 : "))
    if age <0 or age > 150:
        raise Exception("나이는 0이상 150 이하로 작성하세요 ")
except Exception as e:
    print(e) # 어떤 에러가 발생했는지 출력해서 알려달라~ (위에 우리가 설정한 exception을 e로 받아오게 된다.)
else:
    print(f"당신은 {age}살 이군요!") # else 이후는 정상범위일때 출력하는것
finally:
    print("프로그램을 종료합니다. ")
        #finally는 꼭 마지막에 출력해야하는 것
#위에는 예외클래스를 작성하지 않았음

'''
class 클래스이름(부모클래스):
   def __init__(self):
   super().__init__("예외메세지"): 
'''

class AgeError(Exception):
    def __init__(self):
        super().__init__("사람의 나이는 0살 이상, 150 미만으로 작성할 것!")

try:
    age = int(input("나이를 입력하세요 : "))
    if age < 0 or age > 150:
        raise AgeError # 위에 class의 이름을 가져오겠다~ (ageerror가 발생했을때 class 작성해준걸 출력해라~)
except AgeError as e:
    print(e)
else:
    print(f"당신은 {age}살 이군요!")  # else 이후는 정상범위일때 출력하는것
finally:
    print("프로그램을 종료합니다. ")