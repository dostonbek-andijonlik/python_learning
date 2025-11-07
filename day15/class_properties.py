# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
# p1 = Person("Emil", 32)
# print(p1.name)
# print(p1.age)

# class Person: 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Emil", 32)
# print(p1.name)
# print(p1.age)

# p1.age = 43
# print(p1.age)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Emil", 43)

# del p1.age
# print(p1.name)
# print(p1.age)

# class Person:
#     species = "Human" # Class property

#     def __init__(self, name):
#         self.name = name
    
# p1 = Person("Emil")
# p2 = Person("Tobias")

# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)

class Person:
    lastname = ""

    def __init__(self, name):
        self.name = name
    
p1 = Person("Emil")
p2 = Person("Linus")

Person.lastname = "Refsnes"
print()