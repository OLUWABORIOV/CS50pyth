def main():
     print_square(3)

     
def print_square(size):
    # For each row in square
    for i in range(size): 
        print_row(size)

def print_row(width):
    print("#" * width)
         # For each brick in row
         #for j in range(size):
              # print brick
             # print("#", end="")
         #print()


main()




# def main():
#     print_column(3)

# def print_column(height):
#     print("#\n" * height, end="")

# main()




# for _ in range(3):
#     print("#")