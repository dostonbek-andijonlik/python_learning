# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, dictionary)
#                        1. in
#                        2. not in 

word = "APPLE"
letter = input("Guess the letter in the word: ")
# if letter in word:
#     print((f"There is a/an {letter}"))
# else:
#     print(f"There is no {letter}")

if letter not in word:
    print(f"There is no {letter}")
else:
    print(f"There is a/an {letter}")
