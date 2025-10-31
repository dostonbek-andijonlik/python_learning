# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of argument's doesn't matter
#                     1. Positional 2. Default 3. KEYWORD 4. Arbitrary

# def hello(greeting, title, fname, lname):
#     print(f"{greeting} {title}{fname} {lname}")

# hello(greeting="Hello", title="Mr.", lname="Squarepants", fname="SpongeBob")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)