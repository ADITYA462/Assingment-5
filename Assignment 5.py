#!/usr/bin/env python
# coding: utf-8

# Challenge 1: Square Numbers and Return Their Sum
# Implement a class Point that has three properties and a method. All these attributes (properties and methods) should be public.

# Sample properties 1, 3, 5
# 
# Sample method output 35

# In[1]:


class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqsum(self):
        return self.x**2+self.y**2+self.z**2
p=Point(1,3,5)
result = p.sqsum()
print(result)


# 

# Challenge 2: Implement a Calculator Class
# Write a Python class called Calculator by completing the tasks below:

# Input - Pass numbers (integers or floats) in the initializer.
# 
# Output - addition, subtraction, division, and multiplication

# Sample input
# 
# obj = Calculator(10, 94)
# obj.add()
# obj.subtract()
# obj.multiply()
# obj.divide()
# 
# Sample output
# 
#  104 
#  84
#  940
#  9.4

# In[2]:


class calculator:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    
c = calculator(94,10)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())


# In[ ]:





# Challenge 3: Implement the Complete Student Class
# Implement the complete Student class by completing the tasks below
# 
# Task
# 
# 👉 Implement the following properties as private:
# 
# • name
# • rollNumber
# 👉 Include the following methods to get and set the private properties above:
# 
# • getName()
# • setName()
# • getRollNumber()
# • setRollNumber()
# 👉 Implement this class according to the rules of encapsulation.
# 
# Input - Checking all the properties and methods
# 
# Output - Expecting perfectly defined fields and getter/setters

# In[3]:


class student:
    def setName(self,Name):
        self.__Name=Name
    def getName(self):
        return self.__Name
    def setRollnumber(self,Rollnumber):
        self.__Rollnumber=Rollnumber
    def getRollnumber(self):
        return self.__Rollnumber
x=student()
x.setName("ALONE KING")
x.setRollnumber("25")
print("Name :",x.getName())
print("Rollnumber :",x.getRollnumber())


# In[ ]:





# Challenge 4: Implement a Banking Account
# Implement the basic structure of a parent class, Account, and a child class, SavingsAccount.
# 
# Task 1
# 
# 👉 Implement properties as instance variables, and set them to None or 0.
# 
# Account has the following properties:
# 
#     • title
#     • Balance
# SavingsAccount has the following properties:
# 
#     • interestRate
# Task 2
# 
# Create an initializer for Account class. The order of parameters should be the following, where Ashish is the title, and 5000 is the account balance:
# 
# Account("Aditya", 5000)
# 
# Task 3
# 
# Implement properties as instance variables, and set them to None or 0.

# In[4]:


class Account:
    def __init__(self,title=0,balance=0):
        self.title=title
        self.balance=balance
class Savingsaccount(Account):
    def __init__(self,interestRate=0):
        self.interestRate=interestRate
        
x = Account("Aditya",5000)
print(x.title)
print(x.balance)
y = Savingsaccount(5)
print(y.interestRate)


# Challenge 5: Handling a Bank Account
# In this challenge, we will be extending the previous challenge and implementing methods in the parent class and its corresponding child class.
# 
# The initializers for both classes have been defined for you.
# 
# Task 1
# 
# In the Account class, implement the getBalance() method that returns balance.
# 
# Task 2
# 
# In the Account class, implement the deposit(amount) method that adds amount to the balance.
# 
# Sample input
# 
# balance = 2000
# deposit(500)
# getbalance()
# 
# Sample output
# 
# 2500
# 
# Task 3
# 
# In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance.
# 
# Sample input
# 
# balance = 2000
# withdrawal(500)
# getbalance()
# Sample output
# 
# 1500
# 
# Task 4
# 
# In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current balance.
# 
# Sample input
# 
# balance = 2000
# interestRate = 5
# interestAmount()
# 
# Sample output
# 
# 100

# In[5]:


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    def withdrawl(self, amount):
        self.balance = self.balance-amount
    def deposit(self, amount):
        self.balance = self.balance+amount
    def getbalance(self):
        return self.balance
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestrate=0):
        super().__init__(title, balance)
        self.interestrate = interestrate
    def interestamount(self):
        return(self.balance*self.interestrate)/100

x=SavingsAccount("Aditya",2000,5)
print("balance",x.getbalance())
x.deposit(500)
print("balance after deposit:",x.getbalance())
print("balance",x.getbalance())
x.withdrawl(500)
print("balance after withdrawl:",x.getbalance())
print("interestamount:",x.interestamount())


# In[ ]:





# In[ ]:





# In[ ]:




