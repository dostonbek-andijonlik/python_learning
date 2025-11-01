# module = a file containing code you want to include in your program
#          use "import" to include a module (built-in or your own)  
#          useful to break up a large program reusable separate files

# print(dir("math"))

# import math as m
# print(m.pi)

# from math import pi
# print(pi)

# import math
# a, b, c, d, e = 1, 2, 3, 4, 5
# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)
# print(math.e ** e)

import example

# print(example.pi_value)

# result = example.square(2)
# print(result)

result = example.circumference(radius=25)
print(result)