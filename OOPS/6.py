class first:
    def show(self):
        print("show from first")
class second(first):
    def desplay(self):
        print(" display from second ")
f=first()
s=second()
f.show()
s.desplay()
s.show()