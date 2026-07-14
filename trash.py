
#! comprehension
#!
#list = [n for n in range(3,37) if n%2==0]
# list = [n*n if n%2==0 else n**3 for n in range(5,10)]
# print(list)

#[exp for var in coll if cond]
# l = ['even' if i % 2 ==0 else 'odd' for i in range(1,6) ]
# print(l)

s = "happy new year"
#output = [["happy",1],["new",0],["year",1]]
# list = [[ch,ch.count("a")] for ch in "happy new year".split(" ")]
# print(list)

# s = "happy new year"
# dict = {ch:len(ch) for ch in "happy new year".split()}


#! 1.WAP TO EXTRACT ALL THE STRINGS FROM THE TUPLE
# a = ("ansh",1234,"bansal",8369,123,"AB")
# var = lambda n : n if type(n) == str else None
# b = filter(var,a) 
# print(tuple(b))
#!  2.WAP TO EXTRACT ALL THE INTEGER NUMBER 
#FROM THE COLLECTION ONLY IF THE NUMBER HAVING 3 DIGITS
# a = [123,2,4,54,234,12,321]
# var = lambda n : n if len(str(n)) == 3 else None
# b = filter(var ,a)
# print(list(b))
#!WAP to extract all vowels from a list of characters using filter().
# a = ["a","i","r","n","o"]
# f = lambda n : n if n in ["a","e","i","o","u"] else None
# b= filter(f,a)
# print(list(b))
#!assignment
# class InvalidOrderError(Exception):
#     pass

# try:
#     a = int(input("Enter value of a: "))
#     b = int(input("Enter value of b: "))
#     c = int(input("Enter value of c: "))

#     if not (a > b and b > c):
#         raise InvalidOrderError("condition not satisfied")
#     mood = input("Enter your mood (happy/sad): ")

#     if mood == "happy":
#         print("OK")
#     elif mood == "sad":
#         print("Need counseling")
#     else:
#         print("Invalid input")

# except InvalidOrderError as e:
#     print("Error:", e)

# except ValueError:
#     print("Error: Please enter valid integers")

# except Exception as e:
#     print("Unexpected error:", e)
#!List Comprehension
#1. WAP TO GET THE SQUARE OF INDIVIDUAL NUMBER IN THE GIVEN LIST
list_ = [1,2,3,4,5,6]   
# var = lambda n : n**2
# a = map(var,list_)
# print(list(a))
# list_ = [1, 2, 3, 4, 5, 6]
# result = [i**2 for i in list_]
# print(result)

# #2. WAP TO GET THE CUBE OF INDIVIDUAL NUMBER ONLY IF THE NUMBER IS EVEN IN THE GIVEN LIST
# #       list_ = [1,2,3,4,5,6]
# list_ = [1, 2, 3, 4, 5, 6]
# result = [i**3 for i in list_ if i % 2 == 0]
# print(result)

# list_ = [1, 2, 3, 4]
# out = [num ** index for index, num in enumerate(list_)]
# print(out)
#! reverse a string without inbuilt
s = "python is great "
rev = ""
temp = " "
for i in s:
    if i!=" ":
        temp = i + temp
    else:
        rev = rev + temp
        temp = " "
rev +=temp
print(rev)

# #!
# var = lambda c: len(c)**2 if len(c) % 2 == 0 else len(c)**3
# print(var([1, 2, 3, 4]))      # 4² = 16
# print(var((10, 20, 30)))      # 3³ = 27
# print(var("hello"))           # 5³ = 125
# #!
# var = lambda s: len(s)**2 if len(s) % 2 == 0 else len(s)**3
# print(var("python"))   
# print(var("hai"))     
# #!