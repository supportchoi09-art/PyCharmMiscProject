#월화수목 1교시 2교시
'''
1일차 1교시입니다.
1일차 2교시 입니다/
'''

day = 1
while day <=4:  #반복을 할 것이다. (포함되는 요일 수를 넣기)
    classs = 1
    while classs <= 2:
        print(f"{day}일차 {classs}교시 입니다.")  # print('{}일차 {}교시 입니다.'.format(day, time))
        classs += 1  #calsss를 1씩 증가시켜준다.
    day += 1

