# overloading
class money:
    def assign(self,*argv):
        if len(argv)==0:
            self.rs=int(input("enter rs "))
            self.ps=int(input("enter ps"))
            self.tps=self.rs*100+self.ps
        elif len(argv)==1:
            self.tps=int(argv[0])
            self.rs=self.tps//100
            self.ps=self.tps%100
        else:
            self.rs=int(argv[0])
            self.ps=int(argv[1])
            self.tps=self.rs*100+self.ps
    def show(self):
        print(f"rs={self.rs},paise={self.ps},total paise={self.tps}")


m=money()
m1=money()
m2=money()

m.assign(1909)
m1.assign()
m2.assign(10,80)

m.show()
m1.show()
m2.show()
