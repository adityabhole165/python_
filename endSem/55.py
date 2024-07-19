#money using variable length parameter 
class Money:
    def assign(self,*argv):
        if len(argv)==0:
            self.rs=int(input("enter rupeee"))
            self.ps=int(input("enter paise"))
            self.tps=self.rs*100+self.ps
        elif len(argv)==1:
            self.tps=int(argv[0])
            self.rs=self.tps//100
            self.ps=self.tps%100
        else:
            self.rs=int (argv[0])
            self.ps=int (argv[1])
            self.tps=self.rs*100+self.ps
    def show(self):
        print(f"Rs={self.rs}, paise = {self.ps} , total paise= {self.tps}")
        

print("main")
m1=Money()
m1.assign()
m1.show()

m2=Money()
m2.assign(1020)
m2.show()

m3=Money()
m3.assign(12,30)
m3.show()

print("end ")
            
