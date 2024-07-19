n=int(input("how many numbers you want in list ?"))
li=[]
print("enter ",n,"numbers ")
for r in range(n):
    num=int(input())
    li.append(num)
print("list is ",li)
sum=0
for no in li:
    sum+=no
print("adition of all list elements ",sum)
