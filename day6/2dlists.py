fruits = ["apple", "orange", " banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
# print(groceries[0])
# print(groceries[0][1])
for collection in groceries:
    # print(collection)
    for food in collection:
        print(food, end=" ")
    print()