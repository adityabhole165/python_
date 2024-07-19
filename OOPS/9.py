class first:
    def show(self):
        print("show from first")
    def __init__(self):
        print("constructor from first")
    
class second(first):
    def display(self):
        print("display from second")
    def __init__(self):
        print("constructor from second")
        super().__init__()

f=first()
s=second()

f.show()
s.show()
s.display()

