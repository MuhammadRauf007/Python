s1 = int(input("Enter Number"))
s2 = int(input("Enter Number"))
s3 = int(input("Enter Number"))

total_percentage = (100*(s1+s2+s3))/300

if (total_percentage>=40):
    if(s1>=33 and s3 >=33 and s3>=33):
        print("You are passed :",total_percentage)
else:
    print("you are faild ,",total_percentage)