# While loop executes some cde WHILE some condition remains true

# name = input("Enter your name: ")

# if name == "":
#     print("You didn't enter your name!")
# else:
#     print(f"Hello {name}!")

# while name == "":
#     print("You didn't enter your name!")
#     name = input("Enter your name: ")
# print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative!")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old!")

# food = input("Enter your favourite food: ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter your favourite food: ")
# print("bye!")

num = int(input("Enter a number between 1 - 10: "))

while num < 0 or num > 10:
    print("Enter a valid number!")
    num = int(input("Enter a number between 1 - 10: "))
print(f"Your number is {num}")