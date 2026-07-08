import sys

from sayings import hello, goodbye

if len(sys.argv) == 2:
    hello((sys.argv[1]))
    


if __name__ == "__main__":
 main()






# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])