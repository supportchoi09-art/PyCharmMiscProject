'''
비행기는 총 3대 운항
프로그램을 실행하면 (1번째 비행기 탑승 준비!) (이걸 출력할 것임)
비행기는 여권을 가진 사람 2명이 탑승하면 출발함
승객에게 질문을 해야한다. : *번째 고객님 여권이 있나요? (1,0으로 대답을 받을 것)
여권이 없다면 여권이 없어요! (다음 승객 기다리기) 출력
다음 승객에게 다시 여권 유무 물어보기
여권이 있는 승객이 나타나면 *번째 승객이 탑승했어요! 출력 후
한명밖에 안 탔으니까 다시 여권 유무 묻기
여권을 가진 승객 2명이 다 채워졌다면 비행기 출발 후 다음 비행기 운항 (2번째 비행기 탑승 준비!)
'''

'''fly = 1
num = 1
TO = int(input(f"{num}번째 고객님 여권이 있나요? yes(1)/no(0) : "))
while fly <=3:
    num = 1
    while num == 2:
        print(f"{fly}번째 비행기 탑승 준비 완료")
        num += 1
        continue
    if TO == 1:
        continue
    elif TO == 0:
        print("여권이 없어요! 다음 승객 기다리기!")
        break
fly += 1
'''

flight = 1  # 1번째 while에 쓰이는 가장 큰 변수는 while 바깥에 써주기
while flight <= 3:
    print(f"{flight}번째 탑승 준비!")
    passenger = 1 #그냥 고객(탑승 여부 모름)
    count = 0 # 현재 탑승한 사람의 수 // 2번째 while 들어가기 전에 변수 써주고 while 써주기
    while count < 2:
        passport = int(input(f"{passenger}번째 고객님 여권이 있나요? yes(1)/no(0) : "))
        if passport == 0:
            print("여권이 없어요! 다음 승객 기다리기!")
            passenger += 1 # 이렇게 해야 다시 반복문으로 돌아갔을때 숫자가 증가함
            continue
        print(f"{passenger}번째 승객이 탑승했어요!")
        passenger += 1 #2명의 승객이 타야하기 때문에
        count += 1 #여기서는 탑승한 사람도 한명 올려줘야 한다.
    print("비행기 출발!")
    flight += 1
    print()

# 이야 복습 똑바로 해야할듯




