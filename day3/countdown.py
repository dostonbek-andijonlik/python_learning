import time

# time.sleep(3)

# print("TIME IS UP!")

my_time = int(input("Enter your time: "))

# for x in range(1, my_time):
#     print(x)
#     time.sleep(1)
# print("TIME IS UP!")

# for x in range(my_time, 0, -1):
#     print(x)
#     time.sleep(1)

# print("TIME IS UP!")

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     print(f"00:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("TIME IS UP!")

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME IS UP!")