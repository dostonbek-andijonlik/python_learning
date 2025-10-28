# def fun():
#     print("Hello from GF!")
# fun()

# def evenOdd(x):
#     if (x % 2 == 0):
#         return "Even"
#     else:
#         return "Odd"
    
# print(evenOdd(12))
# print(evenOdd(13,8))

# def my_num(x, y = 50):
#     print("x: ", x)
#     print("y: ", y)

# my_num(10)

# def student(fname, lname):
#     print(fname, lname)

# student(fname="Geeks", lname="Practice")
# student(lname="Practice", fname="Geeks")

# def nameAge(name, age):
#     print(f"Hi my name is {name}")
#     print(f"My age is {age}")

# print("Case-1:")
# nameAge("Suraj", 21)

# print("Case-2")
# nameAge(21, "Suraj")

def myFunction(*args, **kwargs):
    print("Non keyword arguments: (*args):")
    for arg in args:
        print(arg)
    
    print("Keyword arguments: (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFunction("Hey", 'Welcome', first='Geeks', mid='for', last='Geeks')
