'''
나이와 학생인지 여부에 따라 티켓 가격 계산하는 프로그램

나이가 20대이고, 학생이라면 성인 요금의 10% 할인된 가격을 적용
나이가 20대인데, 학생이 아니라면 가격 할인 없음
나이가 20세 미만이라면 어린이 요금

학생여부 판단
20세 미만이라면 False, 아니라면 False/ True
'''

#나이 입력받기
age = int(input("나이를 입력하세요 : "))

#학생 여부 판단
student = False if age < 20 or age >= 30 else bool(int(input("학생인가요? (1:예 / 0:아니요)")))
#bool을 입력하면 true false로 인식할 수 있게 된다.

#요금을 설정
#성인은 만원
#학생은 6천원

cost = 10000
child_price = 6000
#할인조건 : 10% 할인 (이 코드 작성) 나이가 20대이고, 학생인 경우만
'''
cost_dis = cost*0.9 if 30 > age >= 20 and student else cost
'''
discount = 20 <= age < 30 and student

# 기본요금 : 20세 이상이면 성인요금, 아니면 어린이 요금
#orign_price = cost if age >= 20 else child_price
basic_price = cost if age >= 20 else child_price

# 최종요금
result = basic_price * 0.9 if discount else basic_price

print("최종 티켓 가격은 : ", int(result), "원 입니다.")
# int 붙이면 소수점 자리 안나옴
