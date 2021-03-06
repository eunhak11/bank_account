from accountclass.acc import Account
def showMenu():
    print("====Bank Menu====\n1. 계좌개설\n2. 입금하기\n3. 출금하기\n4. 전체조회\n6.프로그램 종료\n================\n")

def selectMenu():
    c=int(input("입력: "))
    return c

def openAccount():  # 계좌개설
    print("======계좌개설======\n")
    num=input("계좌번호: ")
    name=input("이름: ")
    bal=int(input("예금: "))
    newacc= Account(num, name, bal)
    print("##계좌개설을 완료하였습니다##")

    return newacc

def deposit(acc_list):  # 입금하기
    print("====입금하기====")
    target = input("입금하실 계좌번호를 입력해주세요: ")
    index = 0
    for i in range(0, len(acc_list)):
        if(acc_list[i].name == target):
            index = i
            break
        elif(i==len(acc_list)):
            print("##찾으려는 계좌가 없습니다##")
            return

    print("계좌이름: " + acc_list[index].name)
    print("계좌잔고: " + str(acc_list[index].balance))
    value = int(input("입금하실 금액을 입력해주세요: "))
    while(value <= 0):
        print("금액 입력이 올바르지 않습니다.")
        value = int(input("입금하실 금액을 입력해주세요: "))

    acc_list[index].balance += value
    print("##계좌잔고: " + str(acc_list[index].balance) + "##")
    print("##입금이 완료되었습니다##")


def withdraw(acc_list):  # 출금하기
    print("====출금하기====")
    target = input("출금하실 계좌번호를 입력해주세요: ")
    index = 0
    for i in range(0, len(acc_list)):
        if(acc_list[i].name==target):
            index = i
            break
        elif(i==len(acc_list)):
            print("##찾으려는 계좌가 없습니다##")
            return

    print("계좌이름: "+acc_list[index].name)
    print("계좌잔고: "+str(acc_list[index].balance))
    value=int(input("출금하실 금액을 입력해주세요: "))
    while(value <= 0):
        print("금액 입력이 올바르지 않습니다.")
        value = int(input("출금하실 금액을 입력해주세요: "))

    acc_list[index].balance-=value
    print("##계좌잔고: "+str(acc_list[index].balance) + "##")
    print("##출금이 완료되었습니다##")

def account_inquiry(acc_list):
    for account in acc_list:
        account.print_info()

    print("==출력되었습니다.==")