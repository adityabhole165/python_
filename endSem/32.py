def power(x,n):
    p=1
    for r in range(n):
        p*=x
    return p
def factorial(n):
    f=1
    for r in range(2,n+1):
        f*=r
    return f
# positional parameter

# x=int(input("enter values for x ="))
# n=int(input("value for n= "))
# p=power(x,n)
# f=factorial(n)

# keyword parameter
p=power(n=9,x=5)
f=factorial(n=9)
ans=p/f
print("The value of the expression is",p,f)