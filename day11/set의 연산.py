#set를 사용하는 이유는 연산을 활용하기 위해서이다. (집합이라는 개념을 기반으로 데이터를 합치거나 뺴기 위해서)
'''
a = {2,3,6}
b = {3,6,9}
교집합은 6과 3이 된다.

& 연산자 사용
intersection() : 교집합을 반환해주는 method이다.
'''

set_a = {1,2,3,4}
set_b = {3,4,5,6}
print(set_a)
print(set_b)

intersection_AandB = set_a.intersection(set_b)
print(intersection_AandB) # 두 그릅의 교집합이 잘 출력됨

and_Aand_B = set_a & set_b
print(and_Aand_B)

'''
과일을 구매했다!
딸기, 오랜지, 체리
내가 좋아하는 과일 : 포도, 오렌지, 딸기
'''
#여기서 공통되는 과일을 골라서 출력할때도 사용 많이 한다.

set_fruits = {"딸기", "오렌지", "체리"}
set_fruites = {"포도", "오렌지", "딸기"}

and_fruits = set_fruits & set_fruites
print(and_fruits) # 교집합이 출력된다.

set_a_2 = {1,2,3,4}
set_b_2 = {3,4,5,6}

'''
| : (shift 누를 상태로 원화 누르기) 파이프 연산자
union() : 이거 사용해서도 합집합을 구할 수 있다. 
'''

union_set = set_a_2 | set_b_2
print(union_set)

union_set2 = set_a_2.union(set_b_2)
print(union_set2)

# 한달 수강생이 800명, 이 800명이 수업에 들어오는 수 (중복되는 사람 빼고 명수만 구하고 싶을때도 사용한다)

'''
- 연산자를 사용 : 차집합
difference() : 이것도 차집합으로 사용한다. 
'''
set_a_3 = {1,2,3,4}
set_b_3 = {3,4,5,6}

diff_set = set_a_3.difference(set_b_3)
print(diff_set) #A-B라는 차집합이 출력된다.

minus_set = set_a_3 - set_b_3
print(minus_set) #이것도 위에와 동일한 차집합값이 출력된다.

'''
add() : 한번에 하나의 요소 추가
update() : "여러개의 요소를 한꺼번에 추가하는 것이다"
'''

set_method = {1,2,3}
set_method.add(4) #이거는 set_method에 4를 추가하겠다는 의미 // 대신 한번에 하나밖에 추가할 수 없다.
print(set_method)

set_method.update({5,6}) # UPDATE는 2개 이상을 추가할 수 있음
print(set_method)

'''
remove : 특정 요소 제거 (요소가 없으면 오류가 난다!!)
discard : 동일하게 특정 요소를 제거해준다. (요소가 없어도 에러가 나지 않는다)
pop : 임의의 요소를 제거하고 반환
clear : 모든 요소 제거 (완전히 다 없애버림)
'''

set_c = {'a','b','c','d','e','f','g','h'}
set_c.remove('a')
print(set_c) #a가 삭제된 채로 출력이 되고 있다.
#set_c.remove("강아지") 없는걸 넣으면 오류뜸
#print(set_c)

set_c.discard('고양이')
print(set_c) # 이렇게 하면 remove는 오류가 나지만 discard는 없으면 무시하고 출력함

set_red = {"r", "e","d"}
print(set_red)
print(set_red.pop()) #r을 삭제하겠다고 암시
print(set_red) #r이 삭제되고 나서 나머지 값만 출력됨

set_red.clear()
print(set_red)




