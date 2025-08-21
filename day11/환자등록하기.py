'''
환자를 담을 빈 리스트 생성

몇명의 환자를 등록할 것인지 물어보기1

*번째 환자 이름 : 입력받기
*번째 환자 체온 입력받기

비어있는 환자 리스트에 이름과 체온 튜플로 추가하기
'''

patient = []
q = int(input("몇 명의 환자를 등록하시겠습니까?"))

for i in range(q):
    name = input(f"{i+1}번째 환자 이름 : ")
    temp = float(input(f"{i+1}번째 환자 체온 : ")) #소수점으로 받아야하기 때문에
    patient.append((name,temp))

def check_patient(patient_list,fever=37.5):
    print("환자 발열 검사 결과")
    for user, fever_check in patient_list: #이름을 user로 temp를 fever_check로 돌겠다는 의미
        if fever_check >= fever:
            print(f"{user} : {fever_check} 발열 환자 입니다. ")
        elif fever_check <= 36.0:
            print(f"{user} : {fever_check} 저체온증 환자입니다.")
        else:
            print(f"{user} : {fever_check} 정상체온 환자입니다.")

check_patient(patient)

'''
list_patient = []
patient = int(input("몇명의 환자를 등록할 것 입니까? : "))
if patient >0:
    name_patient = input(f"{patient}번째 환자 이름을 입력하세요 : ")
    temp_patient = input(f"{patient}번째 환자 체온을 입력하세요 : ")
    all_patient = (name_patient, temp_patient)
    sorted_patient = sorted(set(all_patient))
    print(sorted_patient)
'''


