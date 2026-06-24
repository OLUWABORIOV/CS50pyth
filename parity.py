def main():
    x = int(input("what's x"))
    if is_even(x):
        print("Even")
    else: 
        print("Odd")

def is_even(n):

    return n % 2 == 0
     #Short Form
     #return True if n % 2 == 0 else False
    #LONG FORM
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

main()






# x = int(input("what's x?"))

# if x % 2 == 0:
#         print("x is even")
# else:
#     print("x is odd")