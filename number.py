def main():
     x = get_int("what's x? ")
     print(f"x is {x}")


def get_int(prompt):   
    while True:
        try:
            return int(input("prompt"))
        except ValueError:
            pass
              #print("x is not an integer")
            
main()

# try:
#     x = int(input("what's x?"))  
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}") #    













# try:
#     x = int(input("what's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")