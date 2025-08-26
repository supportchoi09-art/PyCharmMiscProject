import time

def timer(second,callback):
    #second : 몇초동안 기다릴 것인지를 정하는 것
    #callback : 기다린 후에 실행할 함수를 callback으로 받음
    print("타이머 시작")
    print(f"{second}초 뒤에 요청한 함수를 호출합니다.")

    time.sleep(second)
    # time.sleep(5) : 5초동안 아무작업도 하지 않고 멈춰있게 하는 것이다.
    callback()
    #second에 입력한 초를 기다린 후 콜백으로 전달받은 함수를 실행해주는 구문
    print("타이머 종료")

    #즉, 5초를 기다렸다가 콜백으로 넘어가는 함수를 만든 것이다.

def callback():
    print("5초 뒤 실행될 함수입니다. ")
# 즉 이 함수는 타이머 안에 작동할 함수이다.

timer(5,callback)
# 그래서 우리는 timer 함수를 불러내면 콜백함수가 5초뒤에 실행된다.

'''
타이머 시작
{}초 뒤에 요청한 함수를 호출합니다
{}초 뒤 실행될 함수입니다.
타이머 종료 
'''



