'''
pip install Flask 설치하기 (터미널에서)

'''

from flask import Flask

from bs4 import BeautifulSoup
from urllib import request



app = Flask(__name__) #웹 서버를 생성할게~
weather_url = "http://api.openweathermap.org/data/2.5/weather?" #진짜 기상청 Url 넣을겄! 지금은 임의

@app.route("/")
def hello():
    return "<h1>안녕하세요 </h1>"

@app.route("/setting")
def setting():
    return ("<h1> 설정창으로 들어왔어요!</h1>")

if __name__ ==  "__main__":
    app.run(debug=True) #검사모드로 열겠다
    # 이후 실행하면 생성된 서버기 Running on 으로 뜨고 Control을 누른채로 링크를 눌러주면 열림
    # 그후 /setting 써주면 설정창으로 들어왔어요! 가 뜨는 창을 만들 수 있다.

