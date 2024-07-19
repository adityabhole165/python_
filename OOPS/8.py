class first:
    def show(self):
        print("in show from first ")
    def out(self):
        print("in out from first")

class second(first):
    def display(self):
        print("in display from second ")
        self.out()
    def show(self):
        print("in show from second ")
        super().show()

f=first()
s= second()

f.show()
s.show() 
s.out()
s.show()

