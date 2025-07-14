class sum:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = sum(1)
m = sum(2)

print(n + m)