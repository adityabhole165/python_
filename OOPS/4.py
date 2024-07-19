class mony:
    def __init__(self , r, p):
        self.rs=r
        self.ps=p
        self.tps=r*100+p 
    def show(self):
        print("rs =  ",self.rs)
        print("ps = ",self.ps)
        print("total paise =",self.tps)
m=mony(20,30)
m.show()