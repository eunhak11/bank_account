from accountclass.acc import Account 
def selectMenu():
    print("=====BANK MENU=====\n")
    c=int(input("입력: "))
    return c

def openAccount():
    print("======계좌개설======\n")
    num=input("계좌번호: ")
    name=input("이름: ")
    bal=int(input("예금: "))
    newacc= Account(num, name, bal)
    print("##계좌개설을 완료하였습니다##")

    return newacc

def withdraw(acc_list):
    print("====출금하기====")
    target=input("출금하실 계좌번호를 입력해주세요: ")
    index=0
    for i in range(0,len(acc_list)):
        if(acc_list[i].name==target):
            index=i
            break
        elif(i==len(acc_list)):
            print("##찾으려는 계좌가 없습니다##")
            return

    print("계좌이름: "+acc_list[index].name)
    print("계좌잔고: "+str(acc_list[index].balance))
    value=int(input("출금하실 금액을 입력해주세요: "))
    acc_list[index].balance-=value
    print("##계좌잔고: "+str(acc_list[index].balance))
    print("##출금이 완료되었습니다##")
    