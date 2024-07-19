class MONEY:
    def __init__(self,r,p):
        self.rs=r
        self.ps=p
        self.tps=r*100+p
    def showMoney(self):
        print("rs = ",self.rs)
        print("ps = ",self.ps)
        print("tps = ",self.tps)

print("main")
m=MONEY(10,20)
m.showMoney()
print("end")
        