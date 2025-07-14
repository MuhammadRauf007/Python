class Employe:
    company = "Google"

    def details(self,name,id):
        self.name = name 
        self.id = id

class manager(Employe):
    def salary(self):
        s = int(input("Enter salary"))
        return s

a = Employe()
m = manager()
print(m.company)
m.details("Alex",123)
s = m.salary()
print(m.name,m.id,s)

