# imports
import menues as menu
#from Objects import User,Category,Expense,DB,System
import functions as fun

#main Menu
def main():
    menu.mainMenu()
    while True:
        choice=int(input("Select a Choice: "))
        if choice==1:
#------------------------------------------------------------        
            menu.userMenu()
            while True:
                choice=int(input("Select a Choice: "))
                if(choice==1):
                    fun.addUser()
                    menu.userMenu()
                elif(choice==2):
                    fun.showUser()
                    menu.userMenu()
                elif (choice==3):
                    break
            menu.mainMenu()    
        elif choice==2:
#------------------------------------------------------------
            menu.categoryMenu()
            while True:
                choice=int(input("Select a Choice: "))
                if(choice==1):
                    fun.addCategory()
                    menu.categoryMenu()
                elif(choice==2):
                    fun.showCategory()
                    menu.categoryMenu()
                elif (choice==3):
                    break
            menu.mainMenu() 
        elif choice==3:
#------------------------------------------------------------
            menu.expensesMenu()
            while True:
                choice=int(input("Select a Choice: "))
                if(choice==1):
                    fun.addExpense()
                    menu.expensesMenu()
                elif (choice==2):
                    break
            menu.mainMenu()
        elif choice==4:
#------------------------------------------------------------
            menu.reportMenu()
            while True:
                choice=int(input("Select a Choice: "))
                if(choice==1):
                    print("Monthly Report")
                    fun.monthlyReport()
                    menu.reportMenu()
                elif(choice==0):
                    print("Weekly Report")
                    #show report
                    print()
                    menu.reportMenu()
                elif(choice==0):
                    print("Detailed Monthly Report")
                    #show report
                    print()
                    menu.reportMenu()
                elif (choice==2):
                    break
            menu.mainMenu()
        elif choice==5:
            break
    print("See You Soon")
 #------------------------------------------
if __name__ == '__main__':
     main()