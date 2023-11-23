import sys;

print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)
def rec():
    print("hello")
    rec()

#rec()'