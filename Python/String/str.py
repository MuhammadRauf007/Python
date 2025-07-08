a = input("Enter your name : ")
print(a)

newa = a[0:4]  #Muha
n2 = a[-4:-1] #Rau
n3 = a[9:12] #same as [-4:-1] use index number for negitive slicing
print(newa)
print(n2)
print(n3)
n = a[:4]#same as [0:4]
print(n) 
n = a[0:]#same as [0:12]
print(n) 
n=a[0: 7 : 2] #first 7 character then from 0 leave next to then other two till last
print(n)

l = len(a)
print(l)
l = a.endswith("Rauf")
print(l)
l = a.startswith("Rauf")
print(l)
l = a.count("a")
print(l)
l = a.capitalize()
print(l)
l = a.upper()
print(l)
l = a.lower()
print(l)
l = a.find("Rauf")
print(l)


#Practice set

print(f"Good Afternon, {a} ")
n3  =  a.replace("Rauf","rufi")
print(n3)
print(a.find(" "))
print(a.replace("  "," "))
#strings are imutable means if we make change during print statment the orignal variable will not change