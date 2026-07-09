from helo import hello

def test_default():
       assert hello("David") == "hello, world"
       
def test_argument(): 
          assert hello() == "hello, David"

