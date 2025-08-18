#문자열이란 문자들의 묶음을 말한다.
print('python')
print("12345")
 # 이런것들이 다 문자열이다.  문자열에는 인덱스라는 것이 있다. (순서가 있다) - 즉 글자가 줄 서 있다고 생각하면 된다.

text = "안녕하세요"
print(text[0])
print(text[-1]) #뒤에서부터 접근한다.

# 한번 만들어진 문자열은 나중에 코드로 수정할 수는 없다. ex) text[-1] = "?"

'''
대소문자 변환
upper() - 대문자로 변환
lower() - 소문자로 변환 
capitalize() - 첫 글자만 대문자로 변환

문자열 찾기 
fine() - 특정 글자가 어디있는지 찾는 것이다.
count() - 특정 글자가 몇 번 등장하는지 세는 것이다. 

문자열 변경
replaced() - 특정 글자를 다른 글자로 바꾸기 

문자열 나누고 합치기
split() - 특정 기준으로 문자열 나누기 (리스트로 변환이 된다.)
join() - 리스트를 문자열로 합치기

공백 제거하기
strip() - 양쪽공백 제거
lstrip() - 왼쪽공백 제거
rstrip() - 오른쪽 공백 제거 

문자열이 특정 조건을 만족하는지 확인
startswith - 특정 문자로 시작하는가 
endswith - 특정 문자로 끝나는가 
isdigit() - 숫자로만 이루어져있는가
isalpha() - 알파벳으로만 이루어져 있는가
'''

money = "money"
print(money.capitalize()) # 첫글자만 대문자로 출력됨

find_text = "fine text"
print(find_text.find("text")) #text라는게 5번째에서 시작하고 있다고 인덱스 번호를 알려준다.
print(find_text.find("java")) #우리가 찾는게 없으면  -1로 출력됨.

banana = "banana"
print(banana.count("a"))

replace_text = " I like dogs"
print(replace_text.replace("like", "love"))


