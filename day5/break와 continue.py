# break는 while 문을 강제로 종료시킨다.
# while문의 처음 조건으로 이동한다.
# while에서 continue를 만나면 현재 반복을 건너뛰고 다음 조건을 다시 검사한다.

count = 0
while count < 10:
    print(count)
    count += 1
    if count == 5:
        break

# 여기까지는 평범한 웨일문



num = 0
while num < 20:
    num += 1
    if num == 5:
        continue #이러면 5가 안나옴 (5가 나오는 순간 다시 while 조건으로 들어가서 다시 실행하게 된다. )
    print(num, end=" ")
# end=" "를 해주면 오른쪽으로 이어서 뛰어쓰기 한번하고 나열하겠다는 의미이다.



