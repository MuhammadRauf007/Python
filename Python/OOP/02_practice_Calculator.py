class calculator:
    def sum(self,a,b):
        s = a+b
        return s
    
    def Mul(self,a,b):
        m = a*b
        return m

    def div(self,a,b):
        d = a/b
        return d 
    
    def squre(self,a):
        s = a*a
        return s
    
    def cube(self,a):
        s = a*a*a
        return s
    
obj = calculator()
i = 0
while(i!=1):
        
    print("What do you want to do :")
    print("1.Sum")
    print("2.Multiply")
    print("3.Divide")
    print("4.square")
    print("5.cube")
    option = int(input(""))
    if(option == 1):
        n1 = int(input("Enter Number 1 :"))
        n2 = int(input("Enter Number 2 :"))
        res = obj.sum(n1,n2)
        print(f"The sum of {n1} & {n2} = {res}")
    elif(option == 2):
        n1 = int(input("Enter Number 1 :"))
        n2 = int(input("Enter Number 2 :"))
        res = obj.Mul(n1,n2)
        print(f"The Product of {n1} & {n2} = {res}")
    elif(option == 3):
        n1 = int(input("Enter Number 1 :"))
        n2 = int(input("Enter Number 2 :"))
        res = obj.div(n1,n2)
        print(f"The Division of {n1} & {n2} = {res}")
    elif(option == 4):
        n1 = int(input("Enter Number : "))
        res = obj.squre(n1)
        print(f"The square of {n1}  = {res}")
    elif(option == 5):
        n1 = int(input("Enter Number : "))
        res = obj.cube(n1)
        print(f"The cube of {n1}  = {res}")
    else:
        print("Invalid Input")
    
    i = int(input("Do you want to exit 1.Yes  2.No :" ))