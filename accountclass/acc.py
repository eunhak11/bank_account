class Account:
    def __init__(self, number, name, balance):
        self.number = str(number)  # 계좌번호
        self.name = name  # 계좌 소유주
        self.balance = int(balance)  # 잔고

    def print_info(self):
        print("계좌번호 : ", self.number, "/ 이름 : ", self.name, "/ 잔액 : ", self.balance)