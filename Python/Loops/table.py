n = int(input("Enter a number :"))

for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")
else:
    print("This is table using for")
i = 1
while(i<=10):
    print(f"{n} * {i} = {n*i}")
    i += 1
else:
    print("This is table using While loop")