list_in_list = [1,[2,3],"hello", [True, False]]
print(list_in_list) # 우리가 작성한 그대로 출력됨

print(list_in_list[1][1]) # 1번에 있는 1번을 출력하겠다.

python_class = [
    ["철수", "영희", "민수"], #1조
    ["지수", "현우", "나영"], #2조
    ["동현", "수진", "호영"] #3조
]

# 중첩for문으로 출력
for python_class_for in python_class:
    for item in python_class_for:
        print(item)
# 이렇게 작성하면 하나하나 변수들이 한개씩 출력이 된다.

'''
# 1조 출력
print(python_class[0])

# 2조 출력
print(python_class[1])

# 3조의 수진이 출력
print(python_class[2][1])

# 민수 출력
print(python_class[0][2])

# 지수가 로제로 이름을 개명한 후 2조로 출력
python_class[1][0] = "로제"
print(python_class[1][0])
print(python_class[1])
'''

'''
for문으로 list를 도는것
colors라는 리스트에는 red, orange, green, yellow가 있다. 
for 문을 사용하여 colors라는 리스트를 돌기
'''
colors = ["red", "orange", "green", "yellow"]
for colorss in colors:
    print(colorss, end=" ")

