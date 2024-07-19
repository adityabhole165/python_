def show():
    n=60
    print("\n function N ",n )
    def inner():
        n=22
        print("\n in inner function N= ",n )
    print("\n before calling inner function N ",n)
    inner()
    print("\n after calling inner function N ",n)

n=33
print("in main N =",n)
show()
print("after function call N = ",n)
print("END...___")
    