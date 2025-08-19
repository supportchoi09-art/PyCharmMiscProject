student = [
    ["kim","95","  Pizza  "],
    ["lee","80","pasta"],
    ["park","?","  Piano"],
    ["choi","77","pancake"]
]

# for 문을 사용하여 리스트에 접근할 것
print("1) 변수를 만들어서 이름 첫 글자만 대문자로 보여주기")
for student_up in student:
    print(student_up[0:4][0].capitalize())


for i in student:
    name = i[0].capitalize()
    print(name)
        # 선생님 답변
    # 김, 이, 박, 최를 가져오게 된다.


print("2) 점수가 숫자인 학생들의 평균(정수) 구하기 (숫자가 아니면 제외)")
total = 0
count = 0
for i in student:
    score = i[1]
    if score.isdigit():
        total += int(score)
        count += 1
    avg = total // count if count > 0 else 0 #인원수에 1 이상이 들어오면 그제서야 나누기를 실행해라 아니면 0을 출력해라
    print("유효 인원 : ", count, "평균 : ", avg)
