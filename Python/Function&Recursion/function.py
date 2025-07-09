def a():
    print("hello World")
a()
#argument
def b(a):
    sum = a + 5
    print(sum)

b(6)

#return
v1  = int(input("Enter a number :"))
v2  = int(input("Enter a number :"))
def ret(v1,v2):
    sum = v1+v2
    return sum

e = ret(v1,v2)
print(f"The sum of {v1} & {v2} = {e}")