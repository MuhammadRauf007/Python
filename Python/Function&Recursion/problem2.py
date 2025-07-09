#Convert celcius to Fahrenheit 

def convert_to_Fahrenheit(a):
    return ((a * 9/5) + 32)

n = int(input("Enter temprature in Celcius"))
fahrenheit = convert_to_Fahrenheit(n)
print(f"{n} Celcius = {fahrenheit} fahrenheit")

def convert_to_Celcius(a):
    return ((a - 32) * (5/9))

n = int(input("Enter temprature in Fahrenheit"))
celcius = convert_to_Celcius(n)
print(f"{n} fahrenheit  = {celcius} celcius ")