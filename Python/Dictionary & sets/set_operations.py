s1 = {1,3,453,53}
s2 = {3,4,543,345,53}

print(s1.union(s2)) # all values of boths sets
print(s2.intersection(s1)) # same value of s2 from s1
print(s1.difference(s2)) #differnt values of s1 from s2
print(s2.issubset(s1)) # false its not subset of s1
print(s1.isdisjoint(s2)) #false its not super subset of s2
print(s1.symmetric_difference(s2)) #different values of both sets
