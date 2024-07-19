class math:
    def read(self):
        self.n1= int(input("enter n1 = "))
        self.n2= int(input("enter n2 = "))
        self.n3= int(input(" enter n3 ="))
    def cal(self):
        self.sum=self.n1+self.n2+self.n3
        self.avg=self.sum/3
    def __str__(self):
        return(f"sum = {self.sum} , average = {self.avg}")
        
print("main")
m=math()
m.read()
m.cal()
print(m)
print("end of code ")