class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def printName(self):
        print(self.firstname, self.lastname)
    
p1 = Person("Emil", "Oliveira")
p1.printName()

# class Student(Person):
#     pass
# x = Student("Mike", "Olissen")
# x.printName()

# class Student(Person):
#     def __init__(self, firstname, lastname, year):
#         super().__init__(firstname, lastname)
#         self.graduationYear = year

# x = Student("Mike", "Tyson", 2109)
# print(f"{x.firstname} {x.lastname} {x.graduationYear}")

class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationYear = year

    def greet(self):
        print(f"{self.firstname} {self.lastname} {self.graduationYear}")
x = Student("Mike", "Tyson", 2019)
x.greet()