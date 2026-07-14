# arr = [1,2,3]
# arr.append(4)
# arr.insert(0,0)
# print(arr)
# print(len(arr))

# #!1
# class student:
#     college_name = "cgc"
#     course = "aiml"
#     def __init__(self,student_name,student_age):
#         self.name = student_name
#         self.age = student_age
#     def display(self):
#         print(self.name)
#         print(self.age)
                    
# s1 = student("ansh",19)
# s1.display()

# #!2 
# class mobile:
#     def __init__(self,mob_brand,mob_price):
#         self.brand = mob_brand
#         self.price = mob_price
#     def display(self):
#         print(self.brand)
#         print(self.price)
#         print(mobile.category)
#     category = None    
# m1 = mobile("samsungS24",100000)
# m2 = mobile("iphone20",100000)    
# m1.display()
# m2.display()
# # #!
# class shoppingcart:
#     platform_name = None
#     def __init__(self,customer_name,product_list,total_amount):
#         self.customername = customer_name
#         self.productlist = []
#         self.total_amount = 0
#     def 




#!
# class animal:
#     def eat():
#         pass
# class dog(animal):
#     def bark():
#         pass
# obj1 = dog()
# obj1.bark()
# obj1.eat()    
#!
# class resume10th:
#     def __init__(self,s_name,s_age,s_phone,s_percentage):
#         self.name = s_name
#         self.age = s_age
#         self.phone = s_phone
#         self.percent10 = s_percentage
#     def display(self):
#         print(f"{self.name}{self.age}{self.phone}{self.percent10}")
# class resume12th(resume10th):
#     def __init__(self,name,phone,percent10,s_percentage12):
#         super().__init__(name,phone,percent10)
#         self.percent12 = s_percentage12 
#         def display1(self):
#             super().display()
#         print(f"{self.name}{self.phone}{self.percent10}{self.percent12}")

# class resumedegree(resume12th):
#     def __init__(self,name,phone,percent12,percent10,s_cgpa):
#         super().__init__(name,phone,percent12,percent10)
#         self.cgpa = s_cgpa
#     def display2(self):
#         super().display1()
#         print(f"{self.name}{self.phone}{self.percent10}{self.percent12}{self.cgpa}")    

# obj1 = resumedegree("ansh",9518815523,90,88,9.0)
# obj2 = resume12th("ansh",19,9518815523,90,88)
# obj1.display2()
# obj2.display1()        

#!polyphorphism
# class temp:
#     @staticmethod   
#     def add(a,b):
#         print(a+b)
#     @staticmethod
#     def add(a,b,c):
#         print(a+b+c)
# t = temp()
# t.add(9,1,2)



# #!-1 
# from abc import ABC , abstractmethod
# class Bank(ABC):
#   def __init__ (self,account_holder_name,account_number,balance):
#     self.acc_hname=account_holder_name
#     self.bal=balance
#     self.acc_num=self.verify_acc_num(account_number)

#   @staticmethod
#   def verify_acc_num(account_number):
#     if len(str(account_number))== 10 and str(account_number).isdigit():
#       return account_number
#     else:
#       print("Invalid account number")

#   def display(self):
#     print(f"Account Holder {self.acc_hname} having account number {self.acc_num} with a balance of {self.bal}")

#   def deposit(self,amnt):
#     self.bal+=amnt
#     print(f"The amount of {amnt} has been deposited and new balance is {self.bal}")

#   def withdraw(self,amnt):
#     if amnt>self.bal:
#       print("Invalid amount")
#     else:
#       self.bal-=amnt
#       print(f"The amount of {amnt} has been withdrawn and new balance is {self.bal}")

#   @abstractmethod
#   def add_interest(self):
#     pass

# class SavingAccount(Bank):

#   def add_interest(self):
#     interest = self.bal* 0.05   # 5% interest
#     self.bal+=interest
#     print(f"Interest Added (5%): {interest}")
#     print(f"New Balance: {self.bal}")

# class CurrentAccount(Bank):

#   def add_interest(self):
#     interest = self.bal* 0.08   # 5% interest
#     self.bal+=interest
#     print(f"Interest Added (8%): {interest}")
#     print(f"New Balance: {self.bal}")


# #c1 = CurrentAccount()
# c2 = SavingAccount("ANSH",9518815523,100000000)    
# c2.deposit(1000000000000)
# c2.withdraw(100)    


#!Create a Calculator class with an add() method that can:
#!Add 2 numbers
#!Add 3 numbers
#!Add 4 numbers

# ans
# class calculator:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
#     def add(self,a,b,c,d):
#         return a+b+c+d
# obj1 = calculator()
# print(obj1.add(1,2,3,4))
#!q2
#!Question 2: Student Details (Method Overloading)
#!Problem Statement
#!Create a Student class with a display() method that can:
#!Display only the student's name
#!Display name and age
#!Display name, age, and course

# class student:
#     def name(self,student_name):
#         print(student_name)
#     var1 = name
#     def name(self,student_name,student_age):
#         print(student_name)
#         print(student_age)
#     var2 = name    
#     def name_age_course(self,student_name,student_age,student_course):
#         print(student_name)                
#         print(student_age)    
#         print(student_course)
#     var3 = name    
# c1 = student()
# c1.var1("ansh")
# c1.var2("ansh",19)
# c1.var3("ansh",19,"aiml")
#!Question 2: Payment System (Abstraction)
#!Problem Statement
#!Create an abstract class Payment with an abstract method pay().
#!Create child classes:
#!CreditCard
#!UPI
#!NetBanking
#!Implement the pay() method in each child class.
#ans
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card")

class UPI(Payment):
    def pay(self):
        print("Payment made using UPI")

class NetBanking(Payment):
    def pay(self):
        print("Payment made using Net Banking")

c1 = CreditCard()
u1 = UPI()
n1 = NetBanking()

c1.pay()
u1.pay()
n1.pay()



