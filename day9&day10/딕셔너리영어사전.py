english_dict = {
    "pneumonia" : "폐렴",
    "hematouria" : "혈뇨",
    "hypothyroidism" : "갑상선기능저하증",
    "PDA" : "동맥관개존증"
}

user_word = input("영어 단어를 입력해주세요 : ")
#in 연산자를 통해 입력한 단어가 english_dict에 있는지 확인 / 있다면 출력해주기
if user_word in english_dict:
    print(f"{user_word} : {english_dict[user_word]}")
else:
    print(f"{user_word}는 사전에 없습니다.")
    add_values = input("단어의 뜻을 입력해주세요 : ")
    english_dict[user_word] = add_values
#딕셔너리에 영어단어에 우리가 입력한 뜻을 넣어주겠다 (딕셔너리에 추가되는 형태가 만들어짐)
    print(f"{user_word} : {english_dict[user_word]} (사전에 추가되었습니다!)")






'''
for i in english_dict:
    for j in list_english:
        if j in list_english:
            print(english_dict.values())
            break

        else:
            print("해당 단어의 뜻을 찾을 수 없습니다.")
            break
'''
