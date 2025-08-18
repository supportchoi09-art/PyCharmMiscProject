'''
정수를 입력받아서 입력받은 횟수만끔 *번째 안녕하세요
0보다 이하의 수가 입력되었다면 잘못된 입력입니다. 라는 것을 출력
'''

'''
num = int(input("숫자를 입력하세요. : "))
for num in range(num,num+1):
    if num <= 0:
        print("잘못된 입력입니다.")
    for num2 in range(num):
        print("안녕하세요.")
'''


num = int(input("숫자를 입력하세요. : "))
if num <= 0: # for문 전에 if를 먼저 써주는게 좋다!
    print("잘못된 입력입니다. 1이상의 수를 입력하세요~!!")
else:
    for hello in range(num):
        print(f"{hello+1}번째 안녕하세요.") #+1 안해주면 0부터 출력이 된다.


