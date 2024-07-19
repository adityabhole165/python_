class number:
    def __init__(self, n1,n2):
        self.n1=n1
        self.n2=n2
    def showNums(self):
        print(f"Numbers {self.n1},{self.n2}")

class cal(number):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)
        self.sum=self.n1+self.n2
        self.avg=self.sum/2
    def showResult(self):
        self.showNums()
        print(f"Sum={self.sum}, Average={self.avg}")
    
print("main")
f=number(10,20)
s=cal(8,10)
f.showNums()
s.showResult()
print("end")