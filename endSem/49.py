class math:
    def assign(self,a,b,c):
        self.n1=a
        self.n2=b
        self.n3=c
        
        self.sum=self.n1+self.n2+self.n3
        self.avg=self.sum/3
        print(f"{self.sum} , {self.avg}")
    
print("main")
m=math()
m.assign(10,20,30)
print("end")

