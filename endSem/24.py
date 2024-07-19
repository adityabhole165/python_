# average of last 4 elements 

# method 1
# n=int(input("how many numbers you want in list ?"))
# li=[]
# print("enter ",n,"numbers ")
# for r in range(n):
#     num=int(input())
#     li.append(num)
# print("list is ",li)
# sum=0
# for r in range(6,10):
#     sum+=li[r]
# avg=sum/4
# print("average of last 4 elements=",avg)

# method 2
# n=int(input("how many numbers you want in list = "))
# li=[]
# sum=0
# print("enter ",n,"numbers ")
# for r in range(n):
#     no=int(input())
#     li.append(no)
#     if(r>=6):
#         sum+=no
        
# print("list = ",li)
# print("avg of last 4 elements = ",sum/4)

# simple slicing 
# n=int(input("how many numbers you wanted in the list ="))
# li=[]
# sum=0
# print("enter",n,"elements in list ")
# for r in range(n):
#     no=int(input())
#     li.append(no)
# print("list",li)
# # slicing
# for k in li[6:10]:
#     sum+=k
# print("average of last 4 elements = ",sum/4)


# method 4
n=int(input("how many number you want in list = "))
li=[]
sum=0
for j in range(n):
    num=int(input())
    li.append(num)
print("list = ",li)
ans=sum(li[6:])
print("average of last 4 elements = ",ans/4)