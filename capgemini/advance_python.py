
#*1
#! lambda
#var = lambda n:n%2==0
#print(var(5))
#!
# var = lambda n:n**2
# print(var(5))
#!
# var = lambda a,b:a>b
# print(var(2,3))
#!
# var = lambda a,b: "hi" if a>b else "bye"
# print(var(2,5))
#!
# var = lambda n :n*n if n%2==0 else n**3
# print(var(4))
#!
# var = lambda n : n[::-1] if type(n)== str   or type(n)== list or type(n)== tuple else n
# print(var([1,2,3]))
# print(var(123))
#!
# var = lambda a,b:len(a) == len(b)
# print(var("ansh","bansal"))
#*2
# var  = lambda n: f"{n**3} , {n**2}"
# print(var(2))
# #! 
# var = lambda n : n[-1]
# # print(var("ansh"))
#!
# var = lambda a,b:"yes" if a in b else "not"
# print(var("a","ansh"))
# #!
# var = lambda n : n *(n + 1)//2
# print(var(10))
#!
# var = lambda n : ord(n) if n.islower() else (str(ord(n)))[::-1]
# print(var("A"))
# #!.FIND THE MAXIMUM OF TWO NUMBERS USING LAMBDA.
# var = lambda a,b:a if a>b else b
# print(var(2,3))
# #!  
# check = lambda n: 10 < n < 100
#!
#*WAPT RETURN DICT OF INDEX AND ELEMENT PAIR
# l = [3,2,5,7,8]
# d = {}
# for i in range(len(l)):
#     d(i) == l(i)
# print(d)
#################################################################
# n = "my name is ansh"
# f = lambda n : len(n)
# collection = n.split()
# a = map(f,collection)
# print(list(a))
#!
# coll = [1,2,3,4]
# f = lambda n : n%2==0
# a = map(f,coll)
# print(list(a))

#*filter
# coll = [1,2,3,4]
# f = lambda n : n%2==0
# a = filter(f,coll)
# print(list(a))

#*comprehension 
# list = [ i*i if i%2==0 else i**3 for i in range(5,35)]
# print(list)

#!
# s = "happy new year"
# list = [[ch,ch.count("a")] for ch in "happy new year".split()]
# print(list)
#!
# s = "happy new year"
# dict = {ch:len(ch)for ch in "happy new year".split(" ")}
# print(dict)

# #!
# list = [(i,j) for i in (1,2,3) for j in (1,2,3)]
# print(list)
#* homework
#l1 = ["a",8,3.4,89]
#l2 = [10,2.4,"hello",[5,6]]
#dict = {i:j for i in l1 for j in l2 if type(i) in (tuple,str,int,float,complex) and l1.index(i)==l2.index(j)}
#dict = {l1[i]:l2[i] for i in range(len(l1))}
#print(dict)
#!1 WAP TO SQUARE AND CUBE EACH AND EVERY ELEMENT IN THE GIVEN LIST
#list_ = [1,2,3,4]
#output = [[1, 1], [4, 8], [9, 27], [16, 64]]
# var = lambda n : [n**2,n**3]
# res = map(var,[1,2,3,4])
# print(list(res))
#!
# dict = {i:i**2 if i%2==0 else i**3 for i in range(1,8)}
# print(dict)
#!
s="Data science For Business"
#out={'DATA','ecneics','FOR','BUSINESS'}'''
# list = [i.upper() if i[0].isupper()]
# print(list)
# #!
#s = "hii hello howw"
#output - {"howw":4}
##!
# l = ["abcd","nayan","data","aba"]
# #output - {"abcd":"dcba","nayan":5,"data":atad,"aba":3}
# print({i:len(i) if i==i[::-1] else i[::-1]for i in l})
# print({i:len(i) if l.index(i)%2==1 else i[::-1] for i in l})
# #* file handling 
# var = open("ansh.txt","w")
# var.write("hi i am ansh")
# var.close()
# var = open("ansh.txt","a")      
# var.writelines(["ansh ","hi i am anshbansal"])
# var.close()

var = open("ansh.txt","w+")
var.writelines(["hi i am ansh"," i am a student of aiml"])
var.seek(0)
print(var.read())
var.close()


var = open("ansh.txt","a+")
var.writelines(["hi i am ansh"," i am studying python"])
var.seek(0)
print(var.read())
var.close()


var = open("ansh.txt","r+")
print(var.read())
var.writelines(["hi i am ansh"," i am studying python"])
var.close()