marks = {
    "rauf" : 100,
    "hassan" : 90,
    "ahmad" : 80,
 }

print(marks)

print(marks.keys())
print(marks.items(),type(marks))
marks.update({"hassan" : 80,"amir ": 95} )
print(marks)
print(marks.values())
print(marks.get("umer")) #give none if object was not found in dictionary
#print(marks["umer"]) #give error if object was not found in dictionary
p = marks.pop("ahmad")
print(p)
print(marks)
#print(marks.clear())

marks2 = marks.copy()
marks2.update({"Ahmad" : 99})
print(marks2)




