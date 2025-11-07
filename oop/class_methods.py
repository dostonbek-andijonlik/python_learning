# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print("Hello, my name is " + self.name)

# p1 = Person("Emil")
# p1.greet()

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, x, y):
        return x * y
calc = Calculator()

print(calc.add(1, 3))
print(calc.multiply(4, 6))