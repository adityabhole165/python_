def cal(x,n):
    p=x
    f=1
    for r in range(2,n+1):
        p*=x
        f*=n
    return(p,f)


p,f=cal(4,3)
print(p/f)