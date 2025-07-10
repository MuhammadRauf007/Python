with open("Data.txt") as a:
    content1 = a.read()
    print(type(content1))

with open("Poeam.txt") as a:
    content2 = a.read()
    print(type(content2))

if (content1 == content2):
    print("These files are identical")
else:
    print("These files are not identical")