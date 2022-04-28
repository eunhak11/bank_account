from accountclass.acc import Account 

def bankOpen():
    print("======계좌계설======\n")
    num=input("계좌번호: ")
    name=input("이름: ")
    bal=input("예금: ")
    acc(num, name, bal)
    print("##계좌개설을 완료하였습니다##")
    return acc
