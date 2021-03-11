def mainMenu():
    print("Welcome to Expense Tracker\n")
    selection=["Users","Categories","Expenses","Reports","Exit"]
    i=1
    for choice in selection:
        print(i,". ",choice)
        i+=1
    print()    
#sub menues
def userMenu():
    print("Users\n")
    selection=["Add User","View Users","Back"]
    i=1
    for choice in selection:
        print(i,". ",choice)
        i+=1
    print() 
def categoryMenu():
    print("Category\n")
    selection=["Add Category","View Categories","Back"]
    i=1
    for choice in selection:
        print(i,". ",choice)
        i+=1
    print() 
def reportMenu():
    print("Reports\n")
    #selection=["Monthly Report","Detailed Monthly Report","Back"]
    selection=["Monthly Report","Back"]
    i=1
    for choice in selection:
        print(i,". ",choice)
        i+=1
    print() 
def expensesMenu():
    print("Expenses\n")
    selection=["Add Expense","Back"]
    i=1
    for choice in selection:
        print(i,". ",choice)
        i+=1    
    print()