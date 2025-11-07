# class MyClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = MyClass("Emil", 21)
# print(p1.name)
# print(p1.age)

# class Person:
#     pass

# p1 = Person()
# p1.name = "Emil"
# p1.age = 21
# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Emil", 21)
# print(p1.age)
# print(p1.name)

class Person:
    def __init__(self, name, age = 12):
        self.age = age
        self.name = name

p1 = Person("Javlon")
p2 = Person(32, "Polvon")

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)