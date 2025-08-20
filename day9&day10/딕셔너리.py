# 키 : 값(여기 리스트를 집어넣을 수 있음)
# apple : 사과
#시험이나 공부처럼 추상적인 것들도 다 객체라고 하고 객체는 다 키와 값을 가지고 있다. (속성과 속성값을 가지고 있다는 의미)
me = {
    "name": "CHOIJIWON",
    "age" : 24,
    "number" : "010-****-****",
    "class" : ["c언어", "python", "java"]
}

print(me) #줄줄이 쏘세지 처럼 출력이 된다.

tv = {
    "name" : "삼성전자 FullHD",
    "color" : "black",
    "inch" : "40"
}
#list는 인덱스 번호가 있었음 // 딕셔너리는 순서가 있는 구조가 아니다. 그래서 인덱스 번호가 없다. 대신 키값으로 접근 가능
print(me["age"]) #입력한 키에 대한 값을 출력할 수 있게 된다.

#친구목록
friends ={}
friends["도현"] = 19
friends["현종"] = 28
friends["현민"] = 32
friends["소민"] = 32

print(friends)

friends["현민"] = 31
print(friends) #이렇게 출력하면 현민의 값이 32에서 31로 바뀌어서 출력되는 것을 알 수 있다.

del friends["소민"]
print(friends)

friends.clear()
print(friends) #모든 friends를 삭제한다는 것을 알 수 있다.

'''
keys() : 딕셔너리의 모든 키를 뽑아 리스트와 유사하게 반환한다. 
values() : 딕셔너리의 모든 값을 반환
items() : 딕셔너리의 모든 키와 값의 쌍을 반환 
update(other_dict) : 괄호에 다른 딕셔너리의 키-값 쌍을 추가하거나 덮어씀
'''

my_dict = {
    "name" : "kelly",
    "age" : 18,
    "city" : "New York"
}

keys = my_dict.keys()
print(keys) #위에 적어준 값의 키 값만 출력해준다.

#우리가 진짜 리스트처럼 활용을 하고싶다면

lists = list(my_dict.keys()) #리스트로 바꿔주겠다.
print(lists)

values = my_dict.values()
print(values)
lists2 = list(my_dict.values())
print(lists2)

items = my_dict.items()
print(items) # 키랑 값을 모두다 출력해준다. 그게 item

items = list(my_dict.items())
print(items)

my_dict.update({"age":21, "hobby":"drawing"})
print(my_dict)
#그러면 나이는 21살로 바뀌었고 취미가 추가되어 출력되게 된다.
# update : 동일한 키가 있다면 값을 변경해주고 키가 만약 없다면 새롭게 추가해준다.

print(sorted(my_dict)) # 키값을 기준으로 오름차순이 되게 된다.
print(sorted(my_dict.items())) #키랑 값 모두 출력 그리고 오름차순

print(sorted(my_dict, reverse=True))
#이러면 내림차순으로 거꾸로 출력이 된다.(키만 출력됨)





