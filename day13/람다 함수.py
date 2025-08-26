'''

람다함수 = 익명함수
def 함수이름(매개변수):
    return 결과
: 이게 일반적인 함수 형태

=======
lambda 매개변수:return값

'''

def add(x, y):
    return x + y

print(add(5,1))

lambda_add = lambda x, y: x + y
print(lambda_add(5,5))

numbers = list(range(1,21))
print(numbers)

even_numbers = list(filter(lambda x: x%2==0,numbers))  #filter랑 같이 쓰면 검사할 데이터도 return 뒤에 써줘야한다.
#filter(함수, iterable) : 조건에 맞는 요소만 걸러주는 함수이다.
# filter는 리스트를 뽑아 반환해주는 것이 아니라 필요할때 하나씩 꺼내서 쓸 수 있도록 보관
# for문에서 리스트를 i로 도는것과 비슷하다고 생각하면 된다. (조건에 맞는 것들만 i에 보관되는 것과 비슷하다고 생각하면 된다.)

#iterable : 검사할 데이터 (리스트나 튜플이 들어가게 된다.)

#lambda x: x%2==0
# 첫번째 나온 x => 매개변수
# x%2==0  => 이거는 return값  // 맞다면 true를 반환할 것이다.

print(even_numbers)
