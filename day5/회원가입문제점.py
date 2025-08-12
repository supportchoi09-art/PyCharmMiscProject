# 아이디와 비밀번호를 입력받음
# 비밀번호는 숫자
# 아이디와 비밀번호가 모두 일치한다면 로그인 되었습니다.
#  아이디가 맞지 않다면 아이디를 다시 입력해주세요
# 비밀번호가 틀렸다면 비밀번호 불일치
# 만약 둘다 틀렸다면 / 아이디 비밀번호 불일치, 회원가입 하러가기

ID = input("아이디를 입력하세요 : ")
secret = int((input("비밀번호를 입력하세요 : ")))

correct_ID = "sssk"
correct_secret = 1234

if ID == correct_ID and secret == correct_secret:
    print("로그인 되었습니다.") #여기까진 정답
elif ID != correct_ID and secret == correct_secret:
    print("아이디를 다시 입력해주세요")
elif secret != correct_secret and ID == correct_ID:
    print("비밀번호 불일치")
else:
    print("아이디, 비밀번호 불일치 회원가입하러 가기!")
