#새리스트 = [표현식 for 반복문이름 in 반복할 리스트]
numbers = []
for i in range(1,11):
    numbers.append(i)
print(numbers)

number = [i for i in range(1,11)]   #i값을 변형없이 출력하겠다.
print(number)

number = [i+1 for i in range(1,11)]
print(number)

'''우리는 조건도 추가할 수 있다.'''
even_nums = [i for i in range(1,11) if i % 2 == 0]  #만약에 i를 2로 나눈 나머지가 0이라면 i를 그대로 출력해줘
print(even_nums) #이렇게 되면 2,4,6,8,10만 출력된다.

result =[]
for i in range(1,11):
    if i % 2 == 0:
        result.append("짝수")
    else:
        result.append("홀수")
print(result) # 안에 값이 홀수인지 짝수인지 스스로 계산해서 출력값을 준다.

result2 = ["짝수" if i % 2 ==0 else "홀수" for i in range(1,11)] #if else문을 쓰고 싶으면 if문을 먼저 쓰고 그 후 for문 작성
print(result2)

list_in_list = [
    [1,3,5],
    [6,9,12],
    [15,18,21]
]




list_in_list_of_three = []
for i in list_in_list:
    for j in i:
        if j % 3 == 0:
            list_in_list_of_three.append(j)
print(list_in_list_of_three)
            #print(j, end=" ")

list_in_list_of_three2 = [j for i in list_in_list for j in i if j % 3 == 0]
print(list_in_list_of_three2)



#[] / for문
#list_in_list[0][1]
'''
print(list_in_list[0][1])

for i in list_in_list:
    print(i[1]) # 모든 list의 2번째 순서에 있는 숫자를 꺼내오겠다.
'''


