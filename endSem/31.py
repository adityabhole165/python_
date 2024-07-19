print("enter 5 numbers for list ")
li=[]
dict={}
for r in range(5):
    li.append(int(input()))
for v in li:
    n=li.count(v)
    dict[v]=n
print("list=",li)
print("dictionary=",dict)
    