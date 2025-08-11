a = 7
b = 3

if a > b:
    print("a가 b보다 큽니다.")
#콜론 꼭 써주기!!
if a < b:
    print("a가 b보다 큽니다.")
#이 조건이 참이 아니기 때문에 출력되지 않는다.

age =  20
if age >= 20:
    print("성인입니다.")


fruit = "딸기"
if fruit == "banana":
    print("저는 바나나를 좋아해요")
else:
    print("그닥 좋아하지 않아요.")
#else는 다른조건이 들어가지 않는다. 왜냐하면 if에서 아닌 조건 모두를 포함하고 있기 때문이다.

num = -3
if num >= 0:
    print("양수입니다.")
else:
    print("음수입니다.")

#49가 7의 배수인지 확인하는 if문
numb = 49
if numb%7 == 0: #이게 7로 나눈 나머지 값이 0이 맞니? 라고 물어보는 문
    print("7의 배수입니다.")
else:
    print("7의 배수가 아닙니다.")
#드디어 재능을 찾았다. 이제 학교 자퇴해야겠당

#else if = elif

zero = 0
if zero > 0:
    print("0보다 큰 양수입니다.")
elif zero == 0:
    print("0입니다.")
else:
    print("음수입니다.")










