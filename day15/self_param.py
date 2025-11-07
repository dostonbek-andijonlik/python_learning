# class Person:
#     def __init__(self, name):
#         self.name = name

#     def printName(self):
#         print(f"Hello {self.name}")
# p1 = Person("Emil")
# p2 = Person("Tobias")

# p1.printName()
# p2.printName()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print(f"Hello, my name is {self.name}")
#         print(f"Hello, my age is {self.age}")
# p1 = Person("Emil", 23)
# p1.greet()

# class Car:
#     def __init__(self, name, brand, price):
#         self.name = name
#         self.brand = brand
#         self.price = price
    
#     def access_props(self):
#         print(f"{self.name} {self.brand} {self.price}")
# c1 = Car("Sorento", "Toyota", 210000)
# c1.access_props()

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}. "
    
    def welcome(self):
        message = self.greet()
        print(message + "Welcome to our website!")
    
p1 = Person("Emil")
p1.welcome()