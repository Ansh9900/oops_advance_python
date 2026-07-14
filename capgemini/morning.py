# 1.WAP TO SQUARE AND CUBE EACH AND EVERY ELEMENT IN THE GIVEN LIST
# list_ = [1,2,3,4] ===> out = [[1, 1], [4, 8], [9, 27], [16, 64]]
#var  = lambda n : [n*n,n**3]
# a = map(var,[1,2,3,4])
# print(list(a))

#! 2.WAP TO GET THE FOLLOWING OUTPUT
#list_ = [56, 8.7, [1,2,4], 'helloo', 9-9j, [1,2,3,4]]
# out = [1, 1, 3, 6, 1, 4]

#3.WAP TO GET THE FOLLOWING OUTPUT
# n = "hii hello how are you"
# out = [3, 5, 3, 3, 3]
# var = lambda n : len(n)
# a = map(var,n.split())
# print(list(a))

#! 4.CONVERT LIST OF STRINGS TO UPPERCASE
# list_ = ['Hello', 'hii', 'how are you']
# upper = lambda s: s.upper()
# result = list(map(upper, list_))
# print(result)

# 5.CONVERT LIST OF STRINGS TO INTEGERS
# valve = ['1', '2', '34', '4567', '56789']
# var = lambda n : int(n)
# a = map(var,valve)
# print(list(a))

# 6.ADD TWO LISTS ELEMENT-WISE USING Zip()
# a = [1, 2, 3]
# b = [4, 5, 6]
# a = list(zip(a,b))
# print(list(a))

#! 7.WAP TO GET THE FOLLOWING OUTPUT
# l =# 7.WAP TO GET THE FOLLOWING OUTPUT
# l = [123, 34, 24, 512]
# # OUT = [6, 7, 6, 8]
# a = lambda n : sum(n) 
# b = map(a,l) 
# print(list(b))

# 8.STRIP WHITESPACE FROM STRINGS
# raw_strings = ['  apple  ', ' banana ', 'cherry  ']    ## out =  ['apple', 'banana', 'cherry']
# a = lambda n : n.replace(" ","")
# b = map(a,raw_strings)
# print(list(b))

#! 9.PREFIX EACH ITEM WITH ITS INDEX USING ENUMERATE
#items = ['apple', 'banana', 'cherry']
## out = {0: 'apple', 1: 'banana', 2: 'cherry'}

# 10.COUNT_VOWELS  USING A LAMBDA FUNCTION AND MAP.
words = ["hello", "world", "python", "programming"]
# [2, 1, 1, 3]
count_vowels = lambda word: sum(ch in "aeiouAEIOU" for ch in word)
result = list(map(count_vowels, words))
print(result) 