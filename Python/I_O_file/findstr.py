word = "Rauf"

with open("Data.txt") as f:
   content =  f.read()
   if(word in content):
      content = content.replace(word , "*"*len(word))

with open("Data.txt","w") as w:
   w.write(content)