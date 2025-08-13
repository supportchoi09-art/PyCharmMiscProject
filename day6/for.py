#list는 뭐냐하면 a = 15를 저장할 수 있었음 / 나는 11,12,13 도 저장하고 싶으면 이걸 가능하게 하는게 대괄호로 묶은 list
#여러개의 데이터를 하나의 변수에 저장할때 사용하는게 list / for문은 이 list를 저장하기 위한 것

for num_list in ["텀블러", "스크린", ""]: # for (for문 이름) in []
    print(num_list)

a = [6,7,8,9]
for a_list in a:
    print(a_list) # a가 아니라 a_list를 출력하는 것이다
 # 이렇게 쓰면 출력될때 a에 있는 list들이 하나씩 출력된다.

# 안녕하세요 블랙핑크 제니입니다. (로제, 지수, 리사)
black_pink = ["제니", "로제", "지수", "리사"]   #여기서 제니가 0번 로제가 1번 지수는 2번 리사는 3번이 된다.
for black_pink_list in black_pink:
    print(f"안녕하세요 블랙핑크 {black_pink_list}입니다.")
 # 이렇게 코드를 작성하게 되면 list에 있는 것들이 하나씩 출력이 되게 된다.

for char in "apple":
    print(char)
    # 이렇게 출력하게 되면 문자를 쪼개서 하나하나 출력되게 된다. (스펠링이 쪼개져서 출력된다)

# 1~5까지의 정수의 합을 구하고 싶다.
sum = 1+2+3+4+5
# 만약 우리가 100까지 더한다고 했을때는 효율적이지는 않다.

'''
range(start, stop, step):
start(생략가능) : 시작 숫자 (생략하면 기본값은 0이다)
stop : 생성된 숫자의 범위의 끝 (stop에 사용된 앖은 포함하지 않는다 = 만약 stop값에 5를 넣으면 5는 포함되지 않는다는 의미이다.)
step(생략가능 즉, 선택적) : 숫자를 증가시키는 간격 (생략하면 1간격씩 늘어나게 된다.) 
'''

for range_for in range(5):
    print(range_for)
    # 그러면 0,1,2,3,4가 출력되게 된다.

for range_for2 in range(2,6):
    print(range_for2)

for range_for3 in range(1,10,2):
    print(range_for3)
#step의 경우 이전숫자에서 그 수를 더해준다고 생각하면 된다.

for range_for4 in range(10,0,-1): # 1씩 감소하기를 바라는 것임
    print(range_for4)

for range_for5 in range(2,11,2):
    print(range_for5)

# range를 사용해서 1~5까지의 합

total = 0
for range_for6 in range(1,6):
    total += range_for6 # 쌓아주면서 계산하기
print(f"합계 : {total} 입니다.")


fruits = ["apple", "banana", "cherry"]
for range_for7 in range(len(fruits)): # len을 넣어주면 list의 길이로 반환하게 된다. 즉 3을 반환하게 된다.
    print(f"인덱스{range_for7} : {fruits[range_for7]}")

# 구구단 2단 출력

gugu = [1,2,3,4,5,6,7,8,9,10]
for range_for8 in range(len(gugu)):
    print(f"{range_for8} X {2} = {range_for8 * 2}")


 '''
for gugu in range(1:10):
    print(f"{gugu} X {2} = {gugu * 2}") 
 '''

 # 중첩 for을 사용해서 구구단 전체를 만들 수 있다.