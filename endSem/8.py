tm=int(input("enter total marks out of 500 ="))
if(tm<500):
    per=tm/5;
    if(per<45):
        print("fail");
    elif(per<60):
        print("pass");
    elif(per<66):
        print("first class");
    else:
        print("first class with destinction");
else:
    print("invalid total marks:");
    
print("end ")


