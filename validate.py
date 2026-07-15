#re.search()
import re

email = input("what's your email? ").strip()

#if re.search(r"^\w[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email):
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
 
    print("Valid")
else:
    print("Invalid")


































# email = input("what's your email? ").strip()

# username, domain = email.split("@")
# if username and domain.endswith(".edu"):
#     print("Valid ")
# else:
#     print("Invalid")