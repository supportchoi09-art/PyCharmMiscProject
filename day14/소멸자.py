'''
사실 모든 객체를 직접 삭제해주지 않아도 된다.
파이썬에는 쓰레기통이 있기 때문에 알아서 필요 없는 객체를 삭제한다. (자동으로 알아서) : garbage collector
__del__
터지는 것을 메모리 누수라고 한다.  // 메모리 과부화가 와서 메모리 누수가 될 가능성이 있다는 의미이다~
'''

class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w') # filename을 쓰기모드로 오픈할 것이다.
        print(f"{filename}파일을 열었습니다!") # 파일이 정상적으로 열린것을 알려주기 위해서 적어준 것이다.
        #생성자로 이미 파일을 열어버렸음 (파일이 없으면 자동으로 만들어줌)

    def write_data(self,data):
        self.file.write(data)

    def __del__(self):
        self.file.close()
        print("파일을 닫았습니다.")

#소멸자를 사용해서 파일을 직접 닫아주는 것이 필요하다.

handler = FileHandler("del_text.txt")
handler.write_data("hello python")
del handler