'''
상속이란
부모클래스(슈퍼클래스)의 속성과 매서드를 물려받아 사용할 수 있도록 만드는 개념이다.
'''

class Animal:
    def __init__(self,type):
        self.type = type

    def make_sound(self):
        print(f"소리를 냅니다!")

class Dog(Animal): #이러면 animal의 자식 class가 된다.
    def __init__(self,name,breed):
        super().__init__("강아지")
        # 부모class의 생성자(super = animal)을 불러서 self.type = "강아지" 를 넣어준 것과 동일하다.
        #super() => 부모 클래스의 속성과 기능을 가져다 쓰겠다! 라는 의미이다.
        # 그런데 가져다 쓰려고 보니까 type을 설정하는 코드가 있네? 가져다 써야지!


        self.name = name
        self.breed = breed
        #Dog의 생성자 안에 super class 생성자를 만드어서 쓰고 type뿐만 아니라 이름이랑 울음소리도 갖고 태어나길 바라는 것이다.(강아지만들때)

    def make_sound(self):
        print("멍멍 왈왈")
#오버라이딩 (재정의) => 부모클래스에서 정의한 내용을 자식 클래스에서 재정의해서 다시 쓰겠다는 의미이다.
# 즉, 부모것도 있는데 난 내가 바꿔서 쓰겠옹~

dog = Dog("봄이", "말티푸")
print(f"{dog.name}는 {dog.breed}이며, {dog.type} 입니다.")
dog.make_sound()
 # 강아지를 하나 만들 수 있다.


''''''


class Animal:
    def __init__(self,type):
        self.type = type

    def make_sound(self):
        print(f"소리를 냅니다!")

class Cat(Animal): #이러면 animal의 자식 class가 된다.
    def __init__(self,name,breed):
        super().__init__("고양이")
        # 부모class의 생성자(super = animal)을 불러서 self.type = "강아지" 를 넣어준 것과 동일하다.
        #super() => 부모 클래스의 속성과 기능을 가져다 쓰겠다! 라는 의미이다.
        # 그런데 가져다 쓰려고 보니까 type을 설정하는 코드가 있네? 가져다 써야지!


        self.name = name
        self.breed = breed
        #Dog의 생성자 안에 super class 생성자를 만드어서 쓰고 type뿐만 아니라 이름이랑 울음소리도 갖고 태어나길 바라는 것이다.(강아지만들때)

    def make_sound(self):
        print("웨오옹")

cat = Cat("오레오", "턱시도냥이")
print(f"{cat.name}는 {cat.breed}이며, {cat.type} 입니다.")
cat.make_sound()