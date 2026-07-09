names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}") 



















# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())












#with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip())





























 # ask for the user's name
# name = input("what's your name? ")

# # open the file in append mode and write the name to it
# with open("names.txt", "a") as file:
#  file.write(f"{name}\n")

















# names = []

# for _ in range(3):
#     names.append(input("what's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")