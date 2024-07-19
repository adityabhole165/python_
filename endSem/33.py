# returning multiple values from function
def cal(x,n):
    p=1
    for r in range(n):
        p*=x
    f=1
    for r in range(2,n+1):
        f*=r
    return(p,f)


p,f=cal(4,3)
print(p/f)
