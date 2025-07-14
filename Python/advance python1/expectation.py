try:
    a = int(input("Enter a number: "))
    print(a)
    
except Exception as e:
    print(e) 

print("Thank You") #this show the program is not terminate


try:
    a = int(input("Enter a number: "))
    print(a)
    

except ValueError as v:
    print("Heyyyy")
    print(v)
     