def english_quiz(question,answers,name):
    score = 0
    student_answers = []

    for i in range(len(question)):
        ans = input(f"'{question[i]}'의 영어 단어를 입력하세요 :  ") #위의 단어 순서대로 영어단어를 입력하세요가 됨,
            student_answers.append(ans)

        if ans.lower() == answers[i].lower():
            score += 10
    print(f"{name}의 점수는 {score}점 입니다. ")
    print("입력한 답 : ", student_answers)


question = ["사과", "바나나", "체리"] #출제용 한글단어 리스트
answers = ["apple", "banana", "cherry"] #정답리스트

name = input(f"학생 이름을 입력해 주세요 : ")

english_quiz(question,answers,name)

