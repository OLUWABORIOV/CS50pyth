def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")


main()












# while True: # this is an infinite loop, it will run forever
#     n = int(input("What's n?"))
#     if n > 0: # if n is greater than 0, the loop will break
#         break # this will break the loop and exit it

# for _ in range(n): # range function does not let you write to much.                     # for i in [0, 1, 2]:  instead of fillingthe list array to 1000 use range and specify the number
#     print("meow")

# for i in range(3): # range function does not let you write to much.                     # for i in [0, 1, 2]:  instead of fillingthe list array to 1000 use range and specify the number
#     print("meow")
#\n create a new line
#print("meow\n" * 3,end="")




# i = 0 # assign the value of 0 to the variable i
# while i < 3: # i is less than 3, so the loop will run
#     print("meow")
#     i += 1   # This is shorthand for i = i + 1. It is incrementing the value of i by 1 each time the loop runs. So, the first time the loop runs, i will be 1, then 2, and finally 3. When i equals 3, the loop will stop running.





# i = 3 #initialize the variable i with the value 3
# while i != 0: # i does not equal 0, it equals 3
#     print("meow")
#     i = i - 1 # This is 2 mathematically, it is decrementing the value of i by 1 each time the loop runs. So, the first time the loop runs, i will be 2, then 1, and finally 0. When i equals 0, the loop will stop running.