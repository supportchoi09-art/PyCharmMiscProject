students = {
    "철수" : ["수학","과학"],
    "영희" : ["영어","국어"],
    "민수" : ["미술","체육"],
    "지혜" : ["음악","가정"],
}

subject_like = input("어떤 과목을 좋아하는 학생을 찾을까요?")

for name, subject in students.items():
    if subject_like in subject:
        print(f"{name}학생이 {subject}을(를) 좋아해요!")
