'''

붕어빵 클래스를 만든다.
생성자는 어떤 맛인지 고를 수 있다. 그리고 몇 개인지(몇개를 만들것인지 갯수도 정해줘야한다)
making이라는 매서드를 만들어서 **맛 붕어빵 **개 나왔습니다. (프린트 해줄 것)

==> 슈크림, 팥,
'''

'''
breaad = input("무슨 맛 붕어빵을 고르실 건가요?")
bread_num = int(input("몇개의 붕어빵을 고르실 건가요?" "초코, 팥, 슈크림")))
bread_type = ["초코", "팥", "슈크림"]

for i in bread_type:


class bread:
    def __init__(self):
        print("")

class making:
    def bread22(self):
        print(f"{bread_type}맛 붕어빵 {bread_num}개 나왔습니다.")
'''


class FishBread:
    def __init__(self, taste,count):
        self.taste = taste
        self.count = count
    #생성자 완료


    def making(self):
        print(f"{self.taste}맛 붕어빵 {self.count}개 나왔습니다.")

# 붕어빵 만드는 class를 만들었다. 이걸 토대로 직접 붕어빵을 만들어줘야한다.


fish_bread = FishBread("슈크림", 5)
fish_bread2 = FishBread("팥", 2)
fish_bread3 = FishBread("초코", 8)

fish_bread.making()
fish_bread2.making()
fish_bread3.making()


