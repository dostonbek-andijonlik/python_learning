# dictionary = a collection of {key: value} pairs
#               ordered and changeable. NO Duplicates

capitals = {"USA" : "Washington D.C",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India"))

# capitals.update({"Germany": "Berlin"})
# capitals.update({"Germany": "Munich"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# print(keys)

# for value in capitals.values():
#     print(value, end=" ")

items = capitals.items()
for key, value in items:
    print(f"{key}: {value}")