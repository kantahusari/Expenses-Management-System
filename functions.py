from Objects import System
system=System()

#user
#----------------------------------
def addUser():
    user=input("Enter New User: ")
    if(system.addUser(user)):
        print(user," Added")
    else:
        print("Adding failed..")
def showUser():
    lines=system.table("user")
    print("ID\t","User")
    print()
    for row in lines:
        print(row[0],".\t",row[1],"\t")
        #print("_______________")

#category
#----------------------------------
def addCategory():
    category=input("Enter New Category: ")  
    if(system.addCategory(category)):
        print(category," Added")
    else:
        print("Adding failed..")
def showCategory():
    print("ID\t","Category")
    print()
    lines=system.table("category")
    for row in lines:
        print(row[0],". ",row[1])

#expense
#----------------------------------
y=0
m=0
def addExpense():
    global y
    global m
    showUser()
    user=int(input("Select User: "))
    showCategory()
    category=int(input("Select Category: "))
    amount=float(input("Enter Amount: "))
    year=yearTest(input("Enter Year: "))
    month=monthTest(input("Enter Month: "))
    y=year
    m=month
    day=dayTest(input("Enter Day: "))
    y=0
    m=0
    print()
    if(system.addExpense(user,category,amount,day,month,year)):
        print("Expense Added..")
    else:
        print("Adding Failed..")
def showExpenses():
    lines=system.table("expense")
    for row in lines:
        print(row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5]," ",row[6])

#validations
#----------------------------------
def monthTest(number):
    while(True):
        while(number.isdigit()):
            if(int(number)>=1 and int(number)<=12):        
                return int(number)
                break
            else:
                number=input("Enter a Valid Month Number: ")
                while(int(number)<1 and int(number)>12):
                    number=input("Enter a Valid Month Number: ")
                return int(number)
                break
        number=input("Enter a Valid Month Number: ")
def yearTest(number):
    if(len(number)==4 and number.isdigit()):
        return int(number)
    else:
        number=input("Enter a valid Year: ")
        while(len(number)!=4 and number.isdigit()):
            number=input("Enter a valid Year: ")
        return int(number)
def dayTest(number):
    global y
    global m
    while(True):
        while(number.isdigit()):
            while(True):
                if(y%4==0):
                    if(m==2):
                        if(int(number)>=1 and int(number)<=29):
                            return int(number)
                            break
                        else:
                            break
                    elif(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
                        if(int(number)>=1 and int(number)<=31):
                            return int(number)
                            break
                        else:
                            break
                    elif(m==4 or m==6 or m==9 or m==11):
                        if(int(number)>=1 and int(number)<=30):
                            return int(number)
                            break
                        else:
                            break
                else:
                    if(m==2):
                        if(int(number)>=1 and int(number)<=28):
                            return int(number)
                            break
                        else:
                            break
                    elif(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
                        if(int(number)>=1 and int(number)<=31):
                            return int(number)
                            break
                        else:
                            break
                    elif(m==4 or m==6 or m==9 or m==11):
                        if(int(number)>=1 and int(number)<=30):
                            return int(number)
                            break
                        else:
                            break
            number=input("Enter a Valid Day: ")
        number=input("Enter a Valid Day: ")

#reports
#----------------------------------
def monthlyReport():
    showUser()
    user=int(input("Select a User: "))
    month=monthTest(input("Select a Month: "))
    year=yearTest(input("Select a Year: "))
    print()
    #report raw data
    original=system.monthlyReport(user,month,year)
    annual=system.detailedmonthly_report(user,year)
#---------------
    #base user and category
    usertable=system.table("user")
    categorytable=system.table("category")
    
    user_to_print=""
    for record in usertable:
        if record[0]==user:
            user_to_print=record[1]
#create the result
    
    only_category=[]
    for value in categorytable:
        only_category.append(value[1])
    

    result=[]    
    for row in original:
        for record in categorytable:
            if row[0]==record[0]:
                sub=[record[1],row[1]]
                result.append(sub)
    
    annual_category=[]
    for row in annual:
        for record in categorytable:
            if row[0]==record[0]:
                sub=[record[1],row[1]]
                annual_category.append(sub)
    
    #total and occurance year for each category 
    annual_final_result=[]
    for cat in only_category:
        subtotal=0
        counter=0
        for value in annual_category:
            if value[0]==cat:
                subtotal+=value[1]
                counter+=1
        sub=[cat,subtotal,counter]
        annual_final_result.append(sub)
        

    #Final
    final_result=[]
    
    for cat in only_category:
        subtotal=0
        for value in result:
            if value[0]==cat:
                subtotal+=value[1]
            for occurance in annual_final_result:
                average_category=0
                if occurance[1]==cat:
                    average_category=round(subtotal/occurance[2],3)
        sub=[cat,subtotal,average_category]
        final_result.append(sub)
        
        #print(annual_final_result[0],annual_final_result[1],annual_final_result[2],sep=" ")
#print the final result

    print("The report of: ",user_to_print)
    print("For the year: ",year,"and month: ",month)
    print()
    print("Category","Amount","\tPercentage %",sep="\t")
    print("-------------------------------------------")
    totalmonth=0
    for value in final_result:
            totalmonth+=value[1]
    for value in final_result:
        if value[1]==0:
            continue
        else:
            print(value[0],value[1],round(value[1]/totalmonth*100,0),sep="\t\t")
    print("-------------------------------------------")
    print("Total:\t\t",totalmonth)
    print()    

#monthlyReport()
#print(value[0],value[1],round(value[1]/totalmonth*100,0),value[2],sep="\t\t")





'''
def Detailed_Monthly_Report():
    showUser()
    user=int(input("Select a User: "))
    month=monthTest(input("Select a Month: "))
    year=yearTest(input("Select a Year: "))
    print()
    #raw data
    #month base
    original=system.monthlyReport(user,month,year)
    annual=system.detailedmonthly_report(user,year)
    
        #base user and category
    usertable=system.table("user")
    categorytable=system.table("category")
    
    user_to_print=""
    for record in usertable:
        if record[0]==user:
            user_to_print=record[1]
    
    categories=[]
    for index in categorytable:
        categories.append(index[1])
    
    result=[]    
    for row in annual:
        for record in categories:
            if row[0]==record[0]:
                sub=[record[1],row[1]]
                result.append(sub)
    print(result)
        
    
    
Detailed_Monthly_Report()    
'''











