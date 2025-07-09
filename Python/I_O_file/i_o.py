a = open("Read","w")
a.write("Hello")
a.close()

b = open("Read","r")
c = b.read()
b.close() 
print(c)

with open("Read","w") as f:
    f.write("kfsdkljf")

b = open("Read","r")
c = b.read()
b.close() 
print(c) 

