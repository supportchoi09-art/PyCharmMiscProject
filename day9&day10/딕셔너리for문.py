fruit_colors = {
    "red" : "apple",
    "yellow" : "banana",
    "purple" : "blueberry"
}

for i in fruit_colors:
    print(i) # 키 값만 출력하게 된다.

sport_star = {
    "축구" : "손흥민",
    "피겨" : "김연아",
    "수영" : "박태환",
    "펜싱" : "박상현"
}

for i,star in sport_star.items():
    print(i)
    print(star)
    #각각 키와 값으로 돌 수 있다.



sport_list = list(sport_star.keys())
print(sport_list)

sport_list.append("농구")
print(sport_list)

for i in sport_star:
    print(i)
 # 농구는 출력되지 않는다.

 #농구선수 서장훈을 추가하고 싶다.
sport_star["농구"] = "서장훈"
print(sport_list)
print(sport_star.items())

