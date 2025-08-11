# 사용자에게 나이를 입력받음
# 사용자에게 키도 입력 받음
#키가 120이상. 닝;기 10살 이상 탑승 가능
# 탑승여부 True/ false
'''
age = int(input("나이를 입력하세요 : "))
height = int(input("키를 입력하세요 : "))

age_all = age >= 10
height_all = height >= 120

print(age_all and height_all)
'''

heigt = int(input("키를 입력하세요 : "))
age = int(input("나이를 입력하세요 : "))

can_ride = heigt >= 120 and age >= 10
print("놀이기구를 탈 수 있나요?", can_ride)

#숫자는 넣을건데 왜 정수를 붙여줘야 하는가? input은 문자로 들어가기 때문에 문자는 숫자연산을 할 수 없다. 그래서 정수형으로 받을게를 인식을
#시켜줘야 한다.
