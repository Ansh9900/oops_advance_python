####################################################################
#* prime number
#!Task1: Find weather number is prime numbers .
#!Task2: Find all the prime numbers between s and e.
#!Task3: Find the sum of all prime numbers between s and e.
#!Task4: wap to print prime digits of a given numbers
#~ task 1
#^ approach 1 
# num = int(input("enter the number"))
# count = 0
# if(num == 0 or num == 1):
#     print("not prime not composite")
# else:
#     i = 2
#     while(i<num):
#         if(num%i == 0):
#          count+=1  
#         i+=1
# if(count>0):
#    print("composite")
# else:
#    print("prime")         
#^ approach 2 
# import math  
# n = int(input("enter the number"))
# is_prime = True
# i = 2
# while(i*i<=n):
#     if(n%i == 0):
#         is_prime = False
#         break
#     i+=1
# if(is_prime == True):
#     print("prime")
# else:
#     print("composite")    
#~task 2
#todo remember to reset the valve of is_prime 
#todo and remember the special case of 0 and 1
# s = int(input("enter starting no"))
# e = int(input("enter last number"))
# if(s>e):
#     print("invalid input")
# else:
#     for i in range(s,e+1):
#         is_prime = True
#         j = 2 
#         while(j<i):
#             if(i%j == 0):
#                 is_prime = False
#             j+=1
#         if(is_prime == True):
#             print(i)
#         i+=1            
#~task 3
# s = int(input("enter starting no"))
# e = int(input("enter last number"))
# sum = 0
# if(s>e):
#     print("invalid input")
# else:
#     for i in range(s,e+1):
#         is_prime = True
#         j = 2 
#         while(j<i):
#             if(i%j == 0):
#                 is_prime = False
#             j+=1
#         if(is_prime == True):
#             sum = sum + i
#         i+=1            
# print(sum)
#~ task 4
# n = int(input("enter the number"))
# while(n>0):
#     ld = n%10
#     j = 2
#     is_true = True
#     while(j<ld):
#         if(ld%j == 0):
#             is_true = False
#             break
#         j+=1    
#     n = n//10
#     if(is_true == True):
#        print(ld)
#!task5 - Find the sum of all factors (divisors) of a number.
#!task6 -  Multiply all factors of a number.