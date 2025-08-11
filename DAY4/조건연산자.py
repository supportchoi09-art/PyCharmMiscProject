#조건을 검사해서 맞으면 오, 틀리면 x 형식
# 피연산자1 if 조건식 else 피연산자2
#true이면 피연산자1이 출력되고 아니면 피연산자 2가 출력된다.
'''
num1 = 100
num2 = 50

big = num1 if num1 > num2 else num2
print(big)
'''
# 사용자가 좋아하는 숫자가 짝수인지 홀수인지 알아보기!

like_num = int(input("좋아하는 숫자를 입력하세요 : "))
odd = "홀수"
even = "짝수"
result = even if like_num%2 == 0 else odd
print(result)

    #어떤 값을 2나눈 나머지가 0이라면 짝수,

'''
result = even like_num % 2 == 0 else odd
'''
