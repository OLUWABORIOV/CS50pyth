import re

name = input("what's your name?").strip()
if matches := re.search(r"^(.+), *(.+)$", name)
   name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
    #last = matches.groups(1)
    #first = matches.groups(2)
    #name = f"{first} {last}"





















# name = input("what's your name?").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")