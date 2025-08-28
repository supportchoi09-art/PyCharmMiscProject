'''
1. import 파일이름
2. from 파일이름 import 변수, 함수, 클래스 (가져와서 쓸 수 있음)
3. from 파일이름 import * (이 별은 전체 선택자라는 의미이다.)

'''

#import hello

#from hello import self_pr #이거는 hello의 파일에서 self_pr만 가져올게~
#self_pr()
#from hello import my_name # 이게 있어야 뒤에거가 오류가 안남
#my_name("맹구") #이러면 에러가 남 (my_name을 쓴다고 불러오지 않았기 때문)



#hello.self_pr() #함수안에 출력하는 기능이 있다.

#print(hello.water)

#hello.my_name("짱구") # 다른 파일에 있는것에도 접근할 수 있다.

from hello import *
self_pr()
my_name("철수")
print(water)
# 이게 가장 권장하지 않는 방법이다.

# 우리가 만들어둔 hello를 모듈화시켜둔 것이다!!