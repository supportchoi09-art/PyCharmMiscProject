# 파이썬은 자료구조가 다양하다.
'''
a라는 이름에 5와 10, 20을 넣고 싶다. 즉, 여러가지 것들을 하나의 변수에 한번에 집어 넣을 수 있도록 한 것이 list이다.
'''

num = 7
nums = [0,1,2,3] #list는 문자, 논리값, 숫자 등 우리가 원하는 데이터를 자유롭게 넣을 수 있다. []안에 ,로 넣어준다.
alphabets = ['a', 'b', 'c']
boolean_type = [True, False, True] # 논리값 list
greetings = ["Hello", "오늘은 python", "8일째"]

mixed_list = [1, "apple", 3.14, True] # 숫자 문자형 소수, 논리형
print(mixed_list) # list 형식으로 출력된다.

mixed_list[0] = 2  #list에 첫번째 있는 것을 2로 바꿔주겠다.
print(mixed_list)

mixed_list[1] = "mango" # 큰따옴표가 꼭 필요
print(mixed_list)

# 음수인덱스도 존재한다. (끝에서부터 접근하는 방식)

family = ["mother", "father", "sister", "dog"]
print(family[-1]) # 가장 마지막에 있는 단어를 출력하겠다.


'''
list[start:end:step] # start는 포함하고 end는 포함하지 않음. step은 간격 (생략시 1)
'''
numbers = [10,20,30,40,50]
print(numbers[0:3]) # 3개를 추출하겠다.
print(numbers[- 2:]) # 끝까지 출력하겠다 (40,50)

print(numbers[::2]) # 2개 간격으로 출력하겠다.

'''
numbers[0] = 100
numbers[1] = 200
print(numbers)
# 한꺼번에 바꾸고 싶을때도 있음
'''

numbers[:2] = [100, 200] #0,1번째에 있는 것들을 오르노ㅉㄱ에 있는 변수로 바꾸겠다./
print(numbers)

numbers[:2] = []
print(numbers) # 0,1번째가 비워진 상태로 출력이 되는 것을 알 수 있다.
#index는 각 list에 번호를 나타내는 것 //




