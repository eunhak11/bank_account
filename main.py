from func import *
from func import selectMenu
from func import openAccount

acc_list = []  #account list

while(True):
    choice= selectMenu()
    if(choice == 1):
        acc_list.append(openAccount())

    elif(choice == 2):
        deposit(acc_list)

    elif(choice == 3):
        withdraw(acc_list)

    elif(choice == 4):
        account_inquiry(acc_list)

    # elif(choice == 5):

    elif(choice == 6):
        break

    else:
        print("===잘못된 입력입니다.===")