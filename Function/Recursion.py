import sys;

print(sys.getrecursionlimit())

def rec():
    print("hello")
    rec()

#rec()