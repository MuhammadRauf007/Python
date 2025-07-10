class Employee: # name
    name = "Rauf"
    languague = "Javascript"  # class attribute 
    salary = "1999$"

    def __init__(self): # constructor execute when ever object created
        print("Hello")

    def sum(self, a,b):
        s = a+b
        return s

obj = Employee()
print(f"name = {obj.name}  Salary = {obj.salary}")
c = obj.sum(2,3)
print(f"The sum = {c}")
obj.joinigdate = "12-june"   #object attribute its have more precedence

print(f"name = {obj.name}  Joining date = {obj.joinigdate}")