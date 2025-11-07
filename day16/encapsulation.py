# class Person:
#     def __init__(self, name, age):
#         self.__age = age
#         self.name = name
    
# p1 = Person("Marcus", 32)
# # # print(p1.__age)
# # print(p1.name)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
    
#     def get_age(self):
#         return self.__age
    
# p1 = Person("Robert", 32)
# print(p1.get_age())
# print(p1.name)

# class Person:
#     def __init__(self, name, age):
#         self.__age = age
#         self.name = name
    
#     def get_age(self):
#         return self.__age

# p1 = Person("Federico", 32)
# print(p1.get_age())
# print(p1.name)

# class Person:
#     def __init__(self, name, age):
#         self.__age = age
#         self.name = name
    
#     def get_age(self):
#         return self.__age
    
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be positive")

# p1 = Person("Sundar", 21)
# print(p1.get_age())

# p1.set_age(26)
# print(p1.get_age())

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def set_grade(self, grade):
#         if 0 <= grade <= 100:
#             self.__grade = grade
#         else:
#             print("Grade must be between 0 and 100")
    
#     def get_grade(self):
#         return self.__grade
    
#     def get_status(self):
#         if self.__grade >= 60:
#             return "Passed"
#         else:
#             return "Failed"

# student = Student("Emil")
# student.set_grade(59)
# print(student.get_grade())
# print(student.get_status())


class Student:
    def __init__(self, name):
        self.name = name
    
    def set_grade(self, grade):
        if 0 <= grade <= 100:        
            self.__grade = grade
    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"
    def get_grade(self):
        return self.__grade

student = Student("Name")
student.set_grade(60)
print(student.get_grade())
print(student.get_status())
