'''count = 0
while count < 3: #조건이 참인지 검사
    print(count) #조건이 참이라면 프린트 안에 들어가는 count를 반복하겠다
    #count = count + 1 계속변화하는 count에 1을 더하라는 의미이다.
    count += 1
'''

# 반복문을 사용하여 10부터 5까지 감소하는

count1 = 10
while count1 >= 5:
    print(count1)
    count1 -= 1
# 순서가 매우 중요하다. (코드의 순서가 잘 못 된 것은 아닌지 확인하기)

'''
우리가 가진 돈은 : 5000
아이스크림 : 1000
아이스크림 2번 사먹을 것임
아이스크림을 1번만 사먹었다! 남은 돈 : ??원
2번 사먹음 남은도 ㄴ: ??원
'''

'''money = 5000
ice = 1000
count3 = 0
while money >= ice and money >= 4000:
    money -= ice
    count3 += 1
    print("아이스 크림", count3, "번 사먹었다. 남은돈은", money, "원 이다.")
'''

money = 5000
ice = 1000
icecream_count = 1

while icecream_count <= 2: #아이스크림 2번만 사먹어
    money -= ice
    print(f"아이스크림을{icecream_count}번 사먹었다! 남은돈은 {money}원 ㅠㅠ")
    icecream_count += 1
          # 횟수를 while 조건문으로 넣고 공부할 수 있는 방법이다.

num = 0
while num < 3:
    print(num)
    # 계속 반복하는 무한루프에 들어가게 된다.




