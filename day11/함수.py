#함수는 프로그래밍을 할때 매우 중요한 기능 중 하나이다. // 특정기능을 수행하는 집합이라고 생각하면 된다.
'''
1. 반복적인 코드 제거 및 재새용성이 좋아진다.
2. 어떤 기능을 수행하는 코드인지 한 눈에 파악 가능 (즉, 가독성이 좋아진다. -> 유지보수)
3. 오류추적(디버깅) 효율적 //

def 함수이름() :
    코드 (들여쓰기 해준다음에 코드를 작성하면 된다)
    def는 definition (정의라는 의미를 가지고 있음)
(함수 이름을 짓는거 중요하다)
'''

def hello():
    print("안녕하세요")
    print("저는 안나입니다.")
    print("엘사 동생이에요")
hello()
# 함수 이름을 마지막에 한번 더 작성해줘야 출력이 된다.
# 함수는 출력 눌렀을때 바로 나타나지 않는다.
#파이썬을 들여쓰기에 매우 민감하다.

'''
int hello(){
    print("안녕하세요");    
    return 0;
}
다른언어 코드 
'''

animals = ["강아지", "고양이", "햄스터", "곰", "기린"]
index = 0

def change_animals():
    global index #밖에 있는 내용을 가져올땐 global을 써줘야함
    if index >= len(animals):
        index = 0 #인덱스가 5가 넘어갔을땐 이 if 조건이 발동되어서 다시 강아지로 돌아가는 것이다.
    print(f"동물을 {animals[index]}로 변경합니다.")
    index += 1
change_animals()
change_animals()
change_animals()
change_animals()
change_animals()
change_animals()