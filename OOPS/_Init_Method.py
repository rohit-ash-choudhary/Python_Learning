class TestA:

    def __init__(self,cpu,memory):
        #print("inside init")
        self.cpu=cpu
        self.memory=memory


    def ram(self):
        print("config : ",self.cpu,self.memory )

obj1=TestA('Raezy',14);
obj2=TestA('Nvdia',32);

obj1.ram();
obj2.ram();


