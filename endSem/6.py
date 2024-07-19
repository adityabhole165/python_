tm=int(input("enter here total marks out of 500="))
if(tm<500):
    percentage=tm/5
    
    if(percentage<45):
        print("fail")
    if(percentage>=45):
        if(percentage<=60):
            print("pass class ")
    if(percentage>=60):
        if(percentage<=66):
            print("first class")
    if(percentage>=66):
        print("first class with destinction")
else:
    print("invalid data")



print("end")