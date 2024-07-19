# calling constructor from the second child class"s constructor
# parent class
class first:
    def __init__(self):
        print("The Constructor from the first:")
    def show(self):
        print("Show from the first ")

# Child class
class second(first):
    def display(self):
        print("display from the second class ")
    def __init__(self):
        print("constructor from second ")
        super().__init__()
        

print("main")
f=first()
s=second()
f.show()
s.display()
