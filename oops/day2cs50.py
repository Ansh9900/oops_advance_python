# def main():
#     a,b = get_detail()
#     print(f"my name is {a} and i live in {b}")   
# def get_detail():
#     name = input("name: ")
#     house = input("location: ")
#     return name,house

# if __name__ == "__main__":
#     main()

class Student:
    ...
def main():
    student = get_student()
    print(f"{student.name} lives in {student.house}")


def get_student():
    student = Student()
    student.name = input("name : ")
    student.house = input("house : ")
    return student
main()
