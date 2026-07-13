import csv

name = input("what is your name? ")
home = input("what is your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})





























# import csv
# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
    
#     for student in sorted(students, key=lambda student: student["name"]):
#         print(f"{student['name']} is from {student['home']}")



















# import csv
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)


#     def get_name(student):
#         return student["name"]

#     for student in sorted(students, key=lambda student: student["name"]):
#         print(f"{student['name']} is in {student['home']}")












# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
