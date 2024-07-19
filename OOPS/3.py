class mat:
    def ass(self,a,b,c):
        self.n1=a
        self.n2=b
        self.n3=c
    def cal(self):
        self.sum=self.n1+self.n2+self.n3
    def show(self):
        print("number ar %d,%d,%d"%(self.n1,self.n2,self.n3))
        
m=mat()
m.ass(1,2,3)
m.cal()
m.show()
