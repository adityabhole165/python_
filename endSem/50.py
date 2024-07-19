class math:
    def assign(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3
    def cal(self):
        self.sum=self.n1+ self.n2+self.n3
        self.avg=self.sum/3
    def show(self):
        print(f"numbers are %d ,%d,%d"%(self.n1,self.n2,self.n3))
        print("sum=%d ,avg=%f"%( self.avg,self.sum))
        
print("\n main")
m=math()
m.assign(25,39,7)
m.cal()
m.show()
print("end")