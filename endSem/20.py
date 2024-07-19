list=[13,5,3,2,3,10,5,13,5]
print("list",list)
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)
print("list without duplicates ",new_list)
        