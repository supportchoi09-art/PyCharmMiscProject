# 중첩개수가 2개 이상이라도 중첩이 가능하나 너무 많으면 가독성이 떨어지기 떄문에
# 보통은 이중 중첩에서 많이 사용한다.
row = 1
while row <= 5:
    column = 1
    while column <= 2:
        '''print(f"{row}행 {column}열")'''
        print("{}행, {}열".format(row, column))
        column += 1
    row += 1
    print("")



