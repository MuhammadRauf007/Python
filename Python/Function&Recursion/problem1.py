#fuction to find greater between 3 number

def greater(a,b,c):
    if(a>b and a>c):
        print(f"A have greater value: {a}")
    elif(b>a and b>c):
        print(f"B have greater value: {b}")
    else:
        print(f"C have greater value: {c}")

a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
c = int(input("Enter a number :"))

greater(a,b,c)