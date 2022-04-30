from func import *
from func import selectMenu
from func import openAccount

acc_list=[] #account list

while(True):
    choice= selectMenu()
    if(choice == 1):
        acc_list.append(openAccount())

    elif(choice == 3):
        withdraw(acc_list)
        



