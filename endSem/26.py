# linear  search 
print("enter 5 elements ")
li=[]
for r in range(5):
    n=int(input())
    li.append(n)
print("list = ",li)
s=int(input("enter number to search : "))
for r in range(5):
    if li[r]==s:
        print("element found")
        break
else:
        print("element not present ")