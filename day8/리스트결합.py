list1 = ['a','b','c']
list2 = ['d','e']

list3 = list1 + list2 # 기존리스트 변경 없음
print(list3)

# 기존에 있는거에 추가해줄 수 있음
list1.extend(list2) # 결합하기 때문에(확장을 하기 때문에) 리스트의 원본이 변경된다.
print(list1) # list1에 list2 값도 포함되어 출력이 된다.
 # 기존의 리스트가 변경되면 안되면 이건 사용하면 안된다.

list4 = list2 * 3
print(list4) # list2에 있는 문자들이 3번 반복되어 나온다.


print("리스트의 길이 확인")
result = len(list4)
print(result) # len은 길이를 의미한다.

print("리스트에서 특정 값이 있는지 확인하는 방법")
print('d' in list4) # list4에 d가 있어?


# 리스트에서 특정값의 개수 구하기 (e) list4에서
result2 = list4.count('e') # 새로운 변수값 만들어주기
print(result2)

print("리스트의 최대값, 최소값 구하기")
list5 = [1,2,3,4,5]
print(max(list5)) #list5에서 최대값 출력
print(min(list5))  # list5에서 최소값 출력

# 중첩list가 가능하다.