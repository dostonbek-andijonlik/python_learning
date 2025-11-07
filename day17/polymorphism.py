x = "Hello World"
# print(len(x))

y = ("apple", "banana", "cherry")
# print(len(y))

d = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2019
}

# print(len(d))

# class Car:
#     def __init__(self, brand, name):
#         self.brand = brand
#         self.name = name
    
#     def move(self):
#         print("Drive")


# class Boat:
#     def __init__(self, brand, name):
#         self.brand = brand
#         self.name = name
    
#     def move(self):
#         print("Sail")


# class Airplane:
#     def __init__(self, name, brand):
#         self.name = name
#         self.brand = brand
    
#     def move(self):
#         print("Fly")

# car1 = Car("Ford", "Mustang")
# boat1 = Boat("Diz", "Nui")
# airplane1 = Airplane("Boeing", "777")

# for x in (car1, boat1, airplane1):
#     x.move()

class Vehicle:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    
    def move(self):
        print("Move")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail")
    
class Plane(Vehicle):
    def move(self):
        print("Fly")
    
car1 = Car("Ford", "Mustang")
boat1 = Boat("Soz", "Tez")
plane1 = Plane("Boeing", 777)

for x in (car1, boat1, plane1):
    print(x.brand, end=" ")
    print(x.name, end=" ")

    x.move()