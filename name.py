import sys 

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:#slicing the list to get all arguments except the first one (which is the script name)
    print("hello, my name is", arg)















# import sys 

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])
















# import sys

# try:
#    print("hello, my name is", sys.argv[1])
# except IndexError:
#    print("too few arguments")