class BankAccount:
    def __init__(self, owner, balance = 0): #만들어지는 초기값은 0이다.
        self.owner = owner
        self.balance = balance

    #여기까지가 계좌를 만든것 (계좌 주인 이름과 잔액(balance))


    def deposit(self,amount):
        self.balance += amount #원래 있던 값에 추가를 해주는 방식이기 때문에 연산자를 사용 즉, balance는 현재잔액이라 생각하면 됨.
        print(f"{self.owner}님의 계좌로 {amount}원이 입금되었습니다. 현재 잔액 : {self.balance}원")


        #여기까지가 입금하는 기능


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.owner}님의 계좌로 {amount}원이 출금되었습니다. 현재 잔액 {self.balance}원")
        else:
            print("잔액이 부족합니다.")

#여기까지가 출금하는 기능


    def check_balance(self):
        print(f"{self.owner}님의 현재 계좌 잔액은 {self.balance}원 입니다. ")


bank1 = BankAccount("최산", 10000) #계좌가 만들어진 것이다.
bank1.check_balance()
bank1.deposit(100000)
bank1.check_balance()
bank1.withdraw(50000)
bank1.check_balance()


bank2 = BankAccount("만수르", 10000000000)
bank2.check_balance()
