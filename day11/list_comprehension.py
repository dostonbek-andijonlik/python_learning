# List comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                      [expresion for value in iterable if condition]


doubles = []

# for x in range(1, 11):
#     doubles.append(x * 2)
# print(doubles)

# doubles = [x * 2 for x in range(1, 11)]
# triples = [x * 3 for x in range(1, 11)]
# squares = [x * x for x in range(1, 11)]
# print(squares)

# fruits = ["Apple", "Banana", "Cherry", "Malina"]
# fruit_chars = [fruit[0] for fruit in fruits]
# print(fruit_chars)

# numbers = [1, -2, 3, -4, 5, -6]
# positive_nums = [num for num in numbers if num >= 0]
# print(positive_nums)

grades = [60, 65, 70, 75, 80, 85, 90]
passing_grade = [grade for grade in grades if grade >= 70]
print(passing_grade)