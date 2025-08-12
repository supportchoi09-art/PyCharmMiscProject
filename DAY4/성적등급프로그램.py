#사용자의 점수를 입력받아
#90점 이상이면 A학점
#80점 이상이라면 B학점
#70점 이상이라면 C학점
#60점 이상이라면 D학점
#위 조건에 부합하지 않는다면 재시험!(F학점)

score = int(input("당신의 성적을 입력하세요 : "))
if score >= 90:
    print("당신은 A학점 입니다.")
elif 90 > score >= 80:
    print("당신은 B학점 입니다. ")
elif 80 > score >= 70:
    print("당신은 C학점 입니다.")
elif 70 > score >= 60:
    print("당신은 D학점 입니다.")
else:
    print("당신은 재시험입니다.")

