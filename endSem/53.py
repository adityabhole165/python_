class first:
    def dis(self):
        print("dis from the first class ")

class second(first):
    def show(self):
        print("show from the second class ")
        

print("main")
f=first()
s=second()
f.dis()
s.show()
s.dis()
print("end ......")