n = int(input("Enter n number : "))

def sum(a):
    if(a==0):
        return 0
    else:
        return a + sum(a-1)

t_sum = sum(n)
print(f"Total sum of {n} natural number = {t_sum}")