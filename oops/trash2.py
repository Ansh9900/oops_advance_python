import day2cs50

# class student:
#     def __init__(self):
#         self.name = "ansh"
# s = student()
# s.name = "AB"
# print(s.name)
#         
# class student:
#     def __init__(self):
#         self._name = "ansh"
# s = student()
# #s._name = "AB"
# print(s._name)        

class student:
    def __init__(self):
        self.__name = "ansh"
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name        
s = student()
s.set_name("AB")
print(s.get_name())