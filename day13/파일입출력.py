'''
open -> 파일을 열기 위한 작업 // open("파일이름","모드")

모드
1. "r" : 읽기모드 (read)
2. "w" : 쓰기모드 (write)
3. "a" : 추가모드 (add)

파일읽기
1. 변수명.read():파일 전체 내용 읽기
2. 변수명.readline() : 파일 한 줄씩 읽기
3. 변수명.readlines() : 파일의 모든 줄을 읽어 리스트로 반환
'''

file = open("text.txt","r")
file_read = file.read()
print(file_read)

file2 = open("text.txt","w")
file2.write("I love icecream") # 지금 기존 text파일을 수정해준 것이다.
# 다시 텍스트로 들어가면 "I love icecream"으로 수정이 된 것을 확인할 수 있다.

file2.close() #의도치않게 느려질수도 있기 때문에 파일을 잡아서 사용량을 감소시킬 수 있다. // 파일을 닫지 않으면 가방 열고 다니는 것과
#동일하게 무언가를 흘리게 될 수도 있다.   // 그래서 마무리로 close까지 해줘야한다.

