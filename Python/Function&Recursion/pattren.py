n = int(input("Enter a number of lines "))

def pattren(n):
    for i in range(n,0,-1):
        print("*"*i,end="")
        print("")

pattren(n)