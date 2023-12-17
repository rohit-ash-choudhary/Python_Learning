class Test:
    def config(self):
        print("a","model","name")
        return True


obj1=Test()
obj2=Test()
#print(type(obj1))

print(Test.config(obj1))

print("hello class and object :"+ __name__)