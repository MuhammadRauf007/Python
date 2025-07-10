class company:
    name = "Micrsoft"

    def __init__(self,ename,esalary,elanguage):
        self.ename = ename
        self.esalary  = esalary
        self.elanguage = elanguage

name = input("Enter your name")
salary = int(input("Enter your salary"))
language = input("Enter your language")

obj = company(name,salary,language)     
print(f"CompanyName = {obj.name} Name = {obj.ename} Salary = {obj.esalary} Language = {obj.elanguage}")   