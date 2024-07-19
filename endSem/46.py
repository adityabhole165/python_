def show():
    # global n
    n=60
    print("\n Function N=",n)
    def inner():
        nonlocal n
        n=22
        print("in inner function n  = ",n)
    print("\n before calling inner function N =", n)
    inner()
    print("\n after calling inner function N =",n)
n=33
print("\n in main N= ", n)
show()
print("After function call N = ",n )
print("end ")