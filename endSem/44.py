def show():
    global n
    n+=5
    print("\n fUNction  n:",n)

n=26
print("\n in Main program ")
print("before function call N =",n)
show()
print("after function call N =",n)
n=55
print("before function call N =",n)
show()
print("after function call N =",n)

