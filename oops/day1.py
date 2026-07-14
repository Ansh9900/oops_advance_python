
#! polymorphism
# class number:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
        
#     def __init__(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)
    
# c1 = number(1,2,3)
#! operator overloading
# class student:
#     def __init__(self,marks):
#         self.marks = marks
#     def __add__(self,other):
#         return self.marks + other.marks    
# s1 = student(80)
# s2 = student(90)
# print(s1+s2)        
#!complex number
# class complex:
#     def __init__(self,r,i):
#         self.r = r
#         self.i = i
#     def __add__(self,others):
#         return f"{self.r + others.r},{self.i+others.i}A"
# c1 = complex(2,1)
# c2 = complex(3,1)
# print(c1 + c2)       
#!age compare
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __gt__(self, other):
#         if self.age>other.age:
#             return True
#         else:
#             return False
# p1 = person("tonystark",32)
# p2 = person("spiderman",24) 
# if p1>p2:
#     print(p1.name)
# else:
#     print(p2.name)   
########################################################################
