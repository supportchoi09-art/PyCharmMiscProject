#순서가 있는 데이터의 집합을 표시한다.
# 튜플은 리스트와는 다르게 변하지 않는다. (불변)
'''
튜플은 한번 생성된 후에 요소의 값을 변경하거나 삭제할 수 없다 (특징)
변수명 = (요소1,요소2,요소3) // 만약 여기서 ()를 []로 바꿔주면 list가 된다.
'''

colors = ("red","green","blue")
bools_tuple = (True,False,True)
mix_tuple = ("red",'g',3,True) #혼합도 가능하다

names = ("mo","eun","ji")
first_name = names[0]
second_name = names[1]
third_name = names[2]
print(first_name)
print(second_name)
print(third_name)

#튜플에서도 마이너스 인덱스를 활용할 수 있다.
print(names[-3])

list = [1,2,3]
tuple = (1,2,3)
print(list)
print(tuple)

list[0] = 30
print(list)

'''
tuple[0] = 30
print(tuple) // 이렇게 쓰면 오류가 난다. 
'''

list.append(4)
print(list)

#tuple.append(4)
#print(tuple) // append도 튜플이 사용할 수 있는 속성이 아니다. 튜플은 요소를 변경 및 추가, 삭제가 모두 불가능하다.
# 코드를 안전하게 사용해야할때는 튜플을 사용하는것이 좋다 (안전하게 보관하기 좋다)

multi_tuple = (1,(2,3),[4,5])
print(multi_tuple[2])
print(multi_tuple[1][1])

multi_tuple[2][0] = 3
print(multi_tuple[2]) # 오 이건 가능하네?// 즉 list는 tuple안에 있더라도 수정이 가능하다!

slice_tuple = (3,20,"파이썬",True,"고양이",23)
print(slice_tuple[0:8]) #범위를 벗어났어도 잘 출력이 된다.
print(slice_tuple[8:50]) #아예 범위를 벗어나도 괄호가 출력이 되게 된다.
#print(slice_tuple[10]) / 인덱스로는 안된다.

# 튜플메서드
#count / index (2개가 있다)
#count; 튜플에서 특정값이 몇번 등장하는지 세어주는 것
#index : 특정 값이 처음 등장하는 위치(인덱스)를 찾아줌

count_tuple = (1,2,3,2,2,4,5)
count_of_2 = count_tuple.count(2)
print(count_of_2) # 총 3개가 있는걸 알려준다.

index_tuple = (10,20,30,40,50)
index_of_20 = index_tuple.index(20) #20이 어디있는지 알려줘
print(index_of_20) #2번째 순서인 1에 있다고 알려준다.

print(len(index_tuple)) #몇개 들어있는지 알려주는 거 (총 5개 있어!)
print(40 in index_tuple) # 40이 index_tuple안에 있니? 있으면 True / 없으면 False

tuple1 = (1,2)
tuple2 = (3,4)
print(tuple1 + tuple2) #더하기 연산자로 튜플끼리 합칠 수 있다.

print(tuple1*3) # 튜플도 곱하기를 통해서 반복도 가능하다.

a = 10 #변수
b = 20 #변수
print(f"교환 전 : a{a}, b{b}")
a,b = b,a
# 변수값을 기반으로 튜플 생성
# 괄호가 없어도 ,가 있다면 튜플로 간주함!!!
print(f"교환 후 : a:{a}, b:{b}")
# 튜플은 변하지 않는 자료구조이지만 서로 가지고 있는 값을 교환할 수 있다.

str_banana = "banana"
set_banana = set(str_banana)
print(str_banana[0])
#print(set_banana[0]) 인덱싱을 사용할 수 없다고 나온다.

str_random = "assdfgdfdfdfsdfsadfsd"
str_random = set(str_random)
print(str_random) # 중복된 것이 사라져서 나온다 {}이 안에

sorted_list_change = sorted(set(str_random))
print(sorted_list_change) # sorted를 하게 되면 오름차순 리스트로 변환되게 된다.  (sorted가 새로운 리스트를 만들어주는 애)

