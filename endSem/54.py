# overridding in python
class first():
    def __init__(self):
        print("hello :) i'm the Constructor ")
    def show(self):
        print("show from the first class")
    def out(self):
        print("out from the first class")

class second(first):
    def display(self):
        print("display from the second class ")
        self.out()
    def show(self):
        print("show from the second class ")
        super().show()

print("in main program ")
f=first()
s=second()
#first object calls
f.show()
f.out()
# from second object calls
s.display()
s.show()
s.show()
s.out()
print("end ")