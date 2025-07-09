#in recursion fuction call itself

def a(n):
    if(n==1&n==0):
        return 1
    else:
        return n * a(n-1)

n = int(input("enter a numbe to find factorial :"))
p = a(n)
print(p)

