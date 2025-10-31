# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#           * unpacking operator
#           ARBITRARY

# def sum(*args):
#     # print(type(args))
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(sum(1, 2, 3))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
    
# print(display_name("John", "Doe", "James"))

# def print_adress(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_adress(street="Fake St",
#              city="Kansas",
#              state="MI",
#              zipCode="54321")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")

shipping_label("John", "Doe", "James",
             street="Fake St",
             city="Kansas",
             state="MI",
             zipCode="54321")
