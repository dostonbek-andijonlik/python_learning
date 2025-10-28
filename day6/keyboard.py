num_pad = ((1, 2, 3), 
           (4, 5, 6), 
           (7, 5, 9),
           ("*", 0, "#"))
for keys in num_pad:
    for sign in keys:
        print(sign, end=" ")
    print()