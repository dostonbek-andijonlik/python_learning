# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# //Local
# def func_1(x):
#     x = 1
#     print(x)

# def func_2(x):
#     x = 3
#     print(x)

# func_1()
# func_2()

# //global
# def func_1():
#     print(x)

# def func_2():
#     print(x)

# x = 2
# func_2()
# func_1()

# //Enclosed
# def func_1():
#     x = 1
  
#     def func_2():
#         print(x)
#     func_2()

# func_1()

# Built-in
from math import e
def func_1():
    print(e)
func_1()
