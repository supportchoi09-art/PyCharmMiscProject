 #  사용자의 몸무게 (소수점) 입력 받기
 # 키 입력받기 (170이면 1.7로 입력 받아야함)
 # BMI = 몸무게 / 키 * 키
'''
length = float(input("키를 입력하세요 : "))

weight = float(input("사용자의 몸무게를 입력 하세요 :"))

BMI = weight/ (length * length * 0.0001)
print("당신의 BMI는", BMI, "입니다.")
'''


weight = float(input("몸무게를 입력하세요 : "))
height_cm = float(input("키를 입력하세요 : "))
height_m = height_cm / 100 #cm에서 m로 변환하게 된다.

bmi = weight / (height_m ** 2)
print("당신의 BMI는", round(bmi,1), "입니다.")



