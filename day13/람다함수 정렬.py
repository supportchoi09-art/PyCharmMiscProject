tuple_num = [(1,10),(4,2),(99,6),(5,1),(8,12)]
sorted_tuple1 = sorted(tuple_num)
print(sorted_tuple1) # 첫번째 값을 기준으로 오름차순이 된 것이다.


sorted_tuple = sorted(tuple_num,key=lambda t:t[1])
#함수의 반환값으로 t[1]을 받고 있는 것이다. (리턴값)
#sorted(iterable,key=함수) : iterable인 tuple_num에서 원소를 하나씩 꺼내서 key에 저장된 함수에 보내게 된다.
#sorted가 정렬을 할때 iterable에 들어있는 값을 각각 lambda한테 전달을 한다.
#여기서 의미하는 원소는 튜플이 된다. (1,10),(4,2) etc
#lambda index(1,10):index[1] // return으로 2번째 값을 넘겨주고 있다. // 위에 t에는 (1,10),(4,2) etc에 접근하고 있다.

print(sorted_tuple)
# 이렇게 하면 뒤에 있는 애들을 기준으로 오름차순을 정렬하게 된다.

