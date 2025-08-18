'''
사용자에게 영화이름을 입력받은 후
계속 반복하는 while문 시작
영화 평점 입력받기 (1~5) 사이로
1~5사이의 평점이 입력되었다면
기생충의 평점 : ***** 이런식으로 출력

1부터 5 사이의 숫자를 입력하세요 출력
(만약 이상한 숫자가 입려되었다면)
 => 다시 별점 입력받으러 가기
'''

'''
movie_name = input("영화이름을 입력하세요. : ")
movie_num = int(input("입력하신 영화 평점을 입력하세요. (1~5 사이로 입력할 것) : "))
while True:
    if movie_num > 5 or movie_num < 1:
        print("1부터 5사이의 숫자를 입력하세요.")
        continue  # 여기서 오류가 나네 ㅅㅂ?
    print(f"당신이 말한 {movie_name}의 평점 : {'*'*movie_num}")
    break
'''
movie_name = input("영화이름을 입력하세요. : ")

while True:
    star_input = int(input("입력하신 영화 평점을 입력하세요. (1~5 사이로 입력할 것) : ")) #아하 숫자 입력은 while문 뒤에 쓰기
    if 1<= star_input <= 5:
        print(f"당신이 말한 {movie_name}의 평점 : {'*' * star_input}")
    else:
        print("1부터 5사이의 숫자를 입력하세요.")
        continue
    break

#윈도우키 + . 을 누르면 이모지를 넣을 수 있다.