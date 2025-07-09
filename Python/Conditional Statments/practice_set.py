i1 = int(input("Enter a number :"))
i2 = int(input("Enter a number :"))
i3 = int(input("Enter a number :"))
i4 = int(input("Enter a number :"))

if(i1>i2 and i1>i3 and i1>i4):
    print("i1 is greater")
elif(i2>i1 and i2>i3 and i2>i4):
    print("i2 is greater")
elif(i3>i1 and i3>i2 and i3>i4):
    print("i3 is greater")
else:
    print("i4 is greater")
