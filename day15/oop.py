# class M1:
#     x = 1

# p1 = M1()


# del p1
# print(p1.x)

# class Person:
#     pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)