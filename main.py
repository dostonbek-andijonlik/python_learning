username = input("Enter your username: ")
if len(username) >= 12:
    print("Username is not more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain any spaces")
else:
    print(f"Welcome {username}")