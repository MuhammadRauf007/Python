a = int(input("Enter your age :"))

if(a > 18):
    if(a>50):
        print("special people")
    else:
        print("Your are eligible")
elif(a<0):
    print("Age is not valid")
else:
    print("You are not eligible")