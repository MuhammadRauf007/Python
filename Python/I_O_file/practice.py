with open("Poeam.txt") as a:
    b = a.readlines()
    print(b)
    print(type(b))
    if("Twinkle" in b):
        print("Twinkel is present")
    else:
         print("NOt found")
          
    
