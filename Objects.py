import sqlite3
from contextlib import closing
class User:
    def __init__(self,name):
        self.name=name
    def printN(self):
        print(self.name)

class Category:
    def __init__(self,name):
        self.name=name

class Expense:
    def __init__(self,u,c,amount,month,day,year):
            self.user=User(u)
            self.category=Category(c)
            self.amount=amount
            self.month=month
            self.day=day
            self.year=year
    def viewExpense(self):
        print(" User: ",self.user.name,"\n",
              "Category: ",self.category.name,"\n",
              "Amount: ",self.amount,"\n",
              "Month: ",self.month,"\n",
              "Day: ",self.day,"\n",
              "Year: ",self.year,"\n")

class DB:
    def __init__(self):
        self._database="expensis.sqlite3"
        self.connect()
        self.close()    
    def connect(self):
        self.connection=sqlite3.connect(self._database)
        self.cursor=self.connection.cursor()
        self.connected=True
        return self.cursor
    def close(self):
        self.connection.commit()
        self.connection.close()
        self.connected=False      
    def excute(self,query):
        if not self.connected:
            self.connect()
            self.cursor.execute(query)
            self.cursor.fetchall()
            self.close()
        else:
            self.connect()
            self.cursor.execute(query)
            self.cursor.fetchall()
            self.close()
    def print_table(self,query):
        if not self.connected:
            self.connect()
            table=[]
            data=self.cursor.execute(query)
            lines=data.fetchall()
            for row in lines:
                table.append(row)
            return table
        else:
            table=[]
            data=self.cursor.execute(query)
            lines=data.fetchall()
            for row in lines:
                table.append(row)
            return table
class System:
    def __init__(self):
        self.db=DB()
#user methods
    def addUser(self,name):
        self.db.excute("INSERT INTO user (user_name) VALUES("+"'"+name+"'"+")")
        return True
#category methods
    def addCategory(self,name):
        self.db.excute("INSERT INTO category (category_name) VALUES("+"'"+name+"'"+")")
        return True
#expenses methods
    def addExpense(self,user,category,amount,day,month,year):
        self.db.excute("INSERT INTO expense(user_id,category_id,ammount,day,month,year) VALUES("+str(user)+","+str(category)+","+str(amount)+","+str(day)+","+str(month)+","+str(year)+")")  
        return True
#reports
#retrieve any table
    def table(self,name):
        data=self.db.connect()
        data.execute("select * from ("+"'"+name+"'"+")")
        lines=data.fetchall()
        table=[]
        for row in lines:
            table.append(row)
        return table
#monthly report
    def monthlyReport(self,user,month,year):
        data=self.db.connect()
        data.execute("select category_id, ammount from (expense) WHERE user_id="+str(user)+" and month="+str(month)+" and year="+str(year)+" order by category_id")
        lines=data.fetchall()
        table=[]
        for row in lines:
            table.append(row)
        return table
    def detailedmonthly_report(self,user,year):
        data=self.db.connect()
        data.execute("select category_id, ammount from (expense) WHERE user_id="+str(user)+" and year="+str(year)+" order by category_id")
        lines=data.fetchall()
        table=[]
        for row in lines:
            table.append(row)
        return table

#"select category_id, ammount from expense where user_id="+str(user)+" and month="+str(month)+" and year="+str(year)+" group by category_id"
        



         
            
    
    
    



#-----------
