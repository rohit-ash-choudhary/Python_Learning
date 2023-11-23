            print("Hello")

class Hi(Thread):
    def run(self):
        for i in range(15):
            print("Hi")

tl1=Hello()
tl2=Hi()

tl1.start()

tl2.start()