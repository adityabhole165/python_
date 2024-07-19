# variable length parameter
def csl(*vlp):
    sum=0
    c=0
    for r in vlp:
        sum+=r
        c+=1
    avg=sum/c
    # print(f"numbers are = {n1},{n2},{n3}")
    print(f"Addition ={sum}")
    print(f"Average = {avg}")
    
print("main")
print("with 3 values ")
csl(9,8,7)
print("with 2 values ")
csl(10,20)
print("with 1 values ")
csl(11)
print("with 4 values ")
csl(10,20,30,40)
