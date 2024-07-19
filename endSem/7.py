# tm=int(input("enter the marks out of 500="));
# if(tm<500):
#     per=tm/5;
#     if(per<45):
#         print("fail");
#     else:
#         if(per<60):
#             print("pass ");
#         else:
#             if(per<66):
#                 print("first class");
#             else:
#                 print("first class with distinction");
# else:
#     print("invalid total marks");

# print("end");
tm=int(input("enter marks out of 500="))
if(tm<=500):
    per=tm/5
    if(per<45):
        print("fail")
    else:
        if(per<60):
            print("pass ")
        else:
                print("first class with distinction")
else:
    print("invalid total marks...")
print("end ")
