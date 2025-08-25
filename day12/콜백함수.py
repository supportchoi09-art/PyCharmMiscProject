def greet(name):
    print(f"안녕하세요 {name}님!")

greet("민수")

def callback_function(callback):
    print("이제 콜백함수 실행할거임")
    callback("이수근")

callback_function(greet)


def hello(name):
    print(f"안녕, {name}!")

hello("봄")

#callback : 실행한 다른 함수 (이름을 임의로 정해줌)
#name : 이름을 받을것
#callback 자리에 다른 함수를 넣어주겠다는 의미이다.

def hello_callback(callback,name):
    callback(name) #hello(name)과 같은 뜻이라는 의미이다~

hello_callback(hello, "은지")

def dinner(name):
    print(f"{name}님은 저녁을 먹었습니다.")

def lunch(name):
    print(f"{name}님은 점심을 먹었습니다. ")

def eating_function(eat,name):
    eat(name)
    #밥을 먹는 함수!
    #dinner(name) - a만약 디너로 호출했다면// 즉 함수에다가 함수를 호출할 수 있다. -

eating_function(dinner, "은지")
eating_function(lunch, "현종")
#우리는 디너나 런치를 출력하지 않고 먹는애들을 출력해서 eat에 함수를 넣어준 것이다.
