from func import *
from func import calcLoan

acc_list = []  #account list

while(True):
    showMenu()
    choice= selectMenu()
    if(choice == 1):
        acc_list.append(openAccount())

    elif(choice == 2):
        deposit(acc_list)

    elif(choice == 3):
        withdraw(acc_list)

    elif(choice == 4):
        account_inquiry(acc_list)

    elif(choice == 5):
        loan(acc_list)

    elif(choice == 6):
        print("##프로그램을 종료합니다##")
        break

    else:
        print("===잘못된 입력입니다.===")
    
    calcLoan(acc_list)