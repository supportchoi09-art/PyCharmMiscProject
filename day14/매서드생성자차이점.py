class Person:
    def __init__(self):
        print("생성자가 호출됨!")

class Person2:
    def say_hello(self):
        print("안녕하세요!")

p1 = Person() # Person 함수가 출력된다. (객체가 생성만 되도 호출이 되는것)

p2 = Person2() #생성자가 없고 그냥 매서드이기 때문에 아무것도 출력되지 않는다.
p2.say_hello() #매서드를 직접 호출을 해줘야지 출력이 된다.  (객체 생성과 행동이 있어야 호출이 된다.)
