'''
 국어, 영어, 수학 점수를 다 더하는 함수를 만들것
 total이라는 변수를 만들어서 집어 넣을것

 avg
 avg를 리턴하는 함수 만들기
'''

def all_sub(kor, engli, math):
    total = kor + engli + math
    avg = total / 3 #//를 넣어주면 뒤에 소수점 자리가 안 나타나게 된다.
    return avg

def grade_function(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

kor = int(input("국어점수를 입력하세요 : "))
engli = int(input("영어점수를 입력하세요 : "))
math = int(input("수학점수를 입력하세요 : "))

average = all_sub(kor, engli, math)
grade = grade_function(average) # 위에서 나온 값을 넣어주겠다는 의미 즉, avg가 아닌 average를 넣어준 이유

print(f"평균 점수 : {average:.2f}") # 소수점 2번째 자리까지 끊어주기 위해서는 .2f라고 써주기
print(f"최종 학점 : {grade}")

