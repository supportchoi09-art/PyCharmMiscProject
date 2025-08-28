'''
터미널 : pit install 모듈 이름을 작성할것
ex) pip install Flask(를 사용할 것) ==> 웹 서버를 구축하는 것이다. // Django
pip install beautifulsoup4 -> 웹에서 데이터 불러와서 분석하기 (웹에 있는 데이터를 가져와서 확인한다~ 그리고 활용한다~) / requests
pip install tensorflow (인공지능을 가지고 사용할 수 있는 녀석) // sciktt-learn
cv2 / pillow (영상쪽 외부모듈)
python midi (음악을 또 이용할 수 있다.)

**웹서버는 위에 3개보다 더 다양하게 있다.
'''
from bs4 import BeautifulSoup
from urllib import request
#우리는 request랑 beautifulsoup4 사용할 것
# 웹 크롤링을 할 것이다.

#1. 데이터 수집 목적은 반드시 학습이나 연구를 목표로 사용해야한다.
#2. 악용하면 안된다. (절대 네버) // 사람들이 많이 다니는 웹사이트 크롤링하면 모든 데이터를 제공받기 때문에 (전체 메모리를) 과부화가 온다
# 서버가 과부화가 오게 된다. (즉, 다른 사람들이 접속을 못하게 된다.) 즉, 반복적으로 크롤링하지 않는게 좋다.

weather_url = "기상청 홈페이지"
request.urlopen(weather_url)

with request.urlopen(weather_url) as response:
soup = BeautifulSoup(data, "xml.parser")

for location in soup.select("loca_ta")
    city = location.select_one("local_ta_name").get_text(strip = True)
    print(f"\n{city}")
soup.select("")
soup.select_one()

for i in range(1,5):
    base = f"week{i}_local_ta_"
    normal = location.select_one(base + "normalYear").get_text(strip = True)
    rng = location.select_one(base + "similarRange").get_text(strip = True)
    minv = location.select_one(base + "minVal").get_text(strip = True)
    maxv = location.select_one(base + "maxVal").get_text(strip = True)
    sim = location.select_one(base + "sim").get_text(strip = True)
    print(f"{i}주차 | 평균 {normal}도 | 범위{rng}도 | 최저 {minv}도 | 최고 {maxv}도 | 유사사례 {sim}")