'''
append() : 리스트 마지막에 새로운 요소 추가
insert() : 중간에 추가

sort() : 오름차순(원본 변경)
sort(reverse = True) : 내림차순

remove() ; list 삭제하고 싶다.
pop(index번호 입력) : 특정위치에 있는 요소를 삭제할 수 있다.

join() : 리스트에 새로운 것을 추가해서 하나의 문자열로 바꿔주어서 결합을 한다.
==> 즉, 새로운 연결 문자를 추가해 하나의 문자열로 결합
reverse 역순

'''

append_nums = [1,2,3]
print(f"append() 추가 전 : {append_nums}")
append_nums.append(4)
print(append_nums)

append_nums.insert(0,0) #인덱스 0번에 0을 추가하겠다.
print(f"insert() 추가 후 : {append_nums}")

remove_nums = [1,2,3]
remove_nums.remove(3) #3을 삭제하겠다.
print(remove_nums)

remove_nums.pop(1) #2번째 위치에 있는 요소를 삭제하겠다.
print(remove_nums)

reverse_nums = [2,4,6,8,10]
reverse_nums.reverse() #역순으로 바꿔주는것
print(reverse_nums)

join_text = ['a','b','c']
join_result = "-".join(join_text)
print(join_result) # 문자열로 연결이 된다. 우리가 추가한 -로 연결되어 나온다.

sort_text = ['나', '다', '가', '사', '라']
sort_text.sort()
print(sort_text) # 오름차순으로 변경한다.

numbers = [3,7,8,6,10,4,2,5,0,1]
#print(3 in numbers)
new_list = [] # 비어있는 리스트를 만든다.
for num in numbers:
    if num > 5:
        new_list.append(num)
        #5를 넘는다면 여기 차곡차곡 쌓아줘
new_list.sort()
print(new_list)


# in 연산자
#x in y : x가 y 안에 있으면 True 아니면 False를 반환해준다.

text = "hello world"
print("hello" in text)  # hello가 text 안에 있는가?
print("java" in text)

#바 라는 텍스트가 들어있는 단어들만 새 리스트에 추가
words = ["사과","바나나","포도","딸기","망고","바람","바이올린"]
bar_words = []
for bar_word in words:
    if "바" in bar_word:
        bar_words.append(bar_word) #bar_word에 있는 "바"가 포함된 단어를 bar_words에 넣어라
#bar_words.sort() #bar_words에 차곡차곡 쌓아라
print(bar_words)




