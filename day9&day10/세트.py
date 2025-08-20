#세트는 딕셔너리처럼 순서가 없다.
#세트는 집합 개념과 비슷하다. 서로 다른 값들을 모아서 관리하는 구조이다.
# 같은 값을 여러개 저장해도 한개로 인식?
#세트는 딕셔너리처럼 순서가 없다. 즉 인덱스[] 사용 불가
'''
변수명 = {요소1, 요소2, 요소3}
'''

'''
리스트 : [ ]

딕셔너리 : {
    키 : 값
}

튜플 : ( )


세트 : { }

'''

str = "apple"
list = [1,2,3]
tuple = (1,2,3)

set_str = set(str)
set_list = set(list)
set_tuple = set(tuple)
print("set_str : ", set_str)
#튜플은 순서가 없기 때문에 지가 마음대로 섞어서 주기 때문에 데이터 정리 및 정렬이 되지 않는다.
print("set_list : ", set_list)
print("set_tuple : ", set_tuple)
