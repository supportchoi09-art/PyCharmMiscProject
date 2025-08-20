inventory = {
    "빼빼로" : 10,
    "칙촉" : 3,
    "오예스" : 0,
    "썬칩" : 5
}

#for문으로 받을 것
# 제고가 0이라면 재고가 없습니다
# 5개 미만이라면 재고가 부족합니다
# 위 조건에 걸리지 않는다면 재고충분!

for i, inventory_item in inventory.items():
    if inventory_item == 0:
        print(f"{i}의 재고가 {inventory_item}개로 없습니다.")
    elif inventory_item < 5:
        print(f"{i}의 재고가 {inventory_item}개로 재고가 부족합니다.")
    else:
        print(f"{i}의 재고가 {inventory_item}개로 재고가 충분합니다.")

'''
for i,star in sport_star.items():
    print(i)
    print(star)
    #각각 키와 값으로 돌 수 있다. 
'''

